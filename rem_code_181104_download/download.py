# -*- coding:utf-8 -*-
__date__ = '2018/11/4 15:35'

import redis, os, contextlib, urllib.request, datetime, logging, io, time
from pykafka import KafkaClient
from PIL import Image
from os import environ
from .settings import *

class downloader(object):
    def __init__(self, name, console=None):
        self.handler = None
        self.logger = None
        self.name = name
        self.day_now = datetime.datetime.now().strftime("%Y%m%d")
        self.consumers = {}

        self.load_config()
        if console is not None:
            self.console = console

        self.set_logger()

    def load_config(self):
        self.r = redis.Redis(host=redis_host, port=redis_port)
        self.images_save_path = images_path
        self.client = KafkaClient(hosts=kafka_host)
        self.thumb_folder = thumb_folder
        self.thumb_width = thumb_width
        self.console = str(console) == True
        self.allow_suffix = ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico', '.icon', '.bmp']
        self.download_time_out = int(download_time_out)

    # 设置logger
    def set_logger(self):
        now = datetime.datetime.now().strftime("%Y%m%d")
        if self.handler is None or now != self.day_now:
            self.day_now = now

            log_dir = os.path.join("logs", now)
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)

            self.handler = logging.FileHandler(filename=os.path.join(log_dir, "%s.log" % self.name))
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            self.handler.setFormatter(formatter)

            self.logger = logging.getLogger()
            if self.handler is not None:
                self.logger.removeHandler(self.handler)

            self.logger.addHandler(self.handler)
            self.logger.setLevel(logging.INFO)

            # 是否屏幕输出日志
            if self.console:

                ch = logging.StreamHandler()
                ch.setLevel(logging.INFO)
                ch.setFormatter(formatter)
                self.logger.addHandler(ch)

    # 获取文件的后缀名，包含[.]
    def get_suffix(self, file_name):
        name = os.path.basename(file_name)
        if "." in name:
            return ".%s" % name.split('.')[-1]

        return None

    # 处理下载链接，链接替换，链接问题修改可以放在这里
    def handle_url(self, file_url):
        file_url = file_url.replace("https:///", "https://")
        file_url = file_url.replace("http:///", "http://")

        try:
            # 处理 url链接不以 "http" 开头的问题
            index_of_http = file_url.index("http")
            if index_of_http != 0:
                file_url = file_url[index_of_http:]

        except Exception as e:
            self.logger.error("[handle url failed] %s " % file_url, exc_info=True)

        return file_url

    # 获取consumer
    def get_consumer(self, topic):
        if topic not in self.consumers:
            download_img_topic = self.client.topics[str(topic)]
            consumer = download_img_topic.get_simple_consumer(
                consumer_group=str(kafka_consumer_group),
                consumer_id=str(kafka_consumer_id),
                auto_commit_enable=True,
                auto_commit_interval_ms=1
            )

            self.consumers[topic] = consumer

        return self.consumers[topic]

    # 下载图片 并生成缩略图
    def download_img_with_thumb(self):
        consumer = self.get_consumer('download_img_topic')
        for message in consumer:
            if message is not None:
                try:
                    img_file = message.value
                    check_file = self.check_dowload_image(img_file)
                    if check_file is not None:
                        # 更新日志
                        self.set_logger()
                        self.logger.info("[Begin download image] %s" % img_file)

                        (file_url, file_save_path, img_thumb_path) = check_file
                        with contextlib.closing(urllib.request.urlopen(file_url, timeout=self.download_time_out)) as fimg:
                            im = Image.open(io.BytesIO(fimg.read()))
                            im.convert('RGB').save(file_save_path)

                            (width, height) = im.size
                            if(width > self.thumb_width):
                                height = int(float(self.thumb_width) / width * height)
                                width = self.thumb_width

                            thumb = im.resize((width, height), Image.ANTIALIAS)
                            thumb.save(img_thumb_path)
                except Exception as e:
                    self.logger.error("[down image error] %s " % img_file, exc_info=True)
                    self.r.sadd('down_image_error', img_file)

    # 下载文件（不生成缩略图）
    def download_file(self):
        consumer = self.get_consumer('download_file_topic')
        for message in consumer:
            if message is not None:
                down_file = message.value
                check_file = self.check_download_file(down_file)

                if check_file is not None:
                    # 更新日志
                    self.set_logger()
                    self.logger.info("[Begin download file] %s" % down_file)
                    try:
                        (file_url, file_save_path) = check_file
                        with contextlib.closing(urllib.request.urlopen(file_url, timeout=self.download_time_out)) as fimg:
                            with open(file_save_path, 'wb') as bfile:
                                bfile.write(fimg.read())
                    except Exception as e:
                        self.logger.error("[down file error] %s " % down_file, exc_info=True)
                        self.r.sadd('downfile_error', down_file)

    # 重新下载出错的图片
    def download_error_list(self):
        pass
        # file_url = self.r.spop('downfile_error')
        # while file is not None:
        #     if file is None:
        #         self.logger.info("[no error file to download]")
        #         time.sleep(60)
        #
        #     fileinfo = file_url.split('_____')
        #     file_url = fileinfo[0]
        #     file_save_path = fileinfo[1]
        #
        #     save_dir = os.path.dirname(file_save_path)
        #     if not os.path.exists(save_dir):
        #         os.makedirs(save_dir)
        #
        #     try:
        #         if not os.path.exists(file_save_path):
        #             file_url = self.handle_url(file_url)
        #             with contextlib.closing(urllib.request.urlopen(file_url)) as fimg:
        #                 with open(file_save_path, 'wb') as bfile:
        #                     bfile.write(fimg.read())
        #     except Exception as e:
        #         self.logger.error("[down error list error] %s " % down_file, exc_info=True)


    # 检查下载的文件，并创建下载路径
    def check_download_file(self, info):
        if info is None:
            self.logger.info('no more images to download')
            return None

        fileinfo = info.split('_____')
        file_url = fileinfo[0]
        file_url = self.handle_url(file_url)

        if len((fileinfo)) < 2:
            return None

        file_save_path = fileinfo[1]
        save_dir = os.path.dirname(file_save_path)

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        if not os.path.exists(file_save_path):
            return file_url, file_save_path

        return None

    # 检查要下载的图片是否符合要求，是否是允许下载的类型，是否已经下载过
    def check_dowload_image(self, info):
        check_file = self.check_download_file(info)
        ret = None

        if check_file is not None:
            (file_url, file_save_path) = check_file
            img_thumb_path = file_save_path.replace('uploads', self.thumb_folder)
            img_thumb_folder = os.path.dirname(img_thumb_path)
            if not os.path.exists(img_thumb_folder):
                os.makedirs(img_thumb_folder)

            # 判断图片后缀
            suffix = self.get_suffix(file_save_path)

            if suffix and suffix in self.allow_suffix and not os.path.exists(img_thumb_path):
                ret = file_url, file_save_path, img_thumb_path

        return ret