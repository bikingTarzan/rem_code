# -*- coding:utf-8 -*-
__date__ = '2018/11/4 15:46'

kafka_host="192.168.128.185:9092"
kafka_consumer_group="spider-ymm"
kafka_consumer_id="spider-ymm"

download_img_topic="downfile_queue_with_thumb"
download_file_topic="downfile_queue"

redis_host="127.0.0.1"
redis_port="6379"

images_path="/data/images"
thumb_folder="thumb"
thumb_width="256"
images_url_prefix="/uploads/crawler/"

console=True

download_time_out=10