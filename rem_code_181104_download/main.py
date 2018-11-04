# -*- coding:utf-8 -*-
__date__ = '2018/11/4 15:35'

import optparse
from .download import downloader

def parse_options():
    parser = optparse.OptionParser(
        usage=("usage: %prog [options] -c ControllerName"))
    parser.add_option("-a", "--action", dest="action", default="image",
                      help=("下载图片: image, 下载文件: file ",
                            "[default %default]"))
    parser.add_option("-c", "--console", dest="console", default="None",
                      help=("是否输出日志",
                            "[default %default]"))

    opts, args = parser.parse_args()
    return opts, args

if __name__ == '__main__':
    (opts, args) = parse_options()
    action_name = opts.action
    console = opts.console

    action = None
    if action_name == 'image':
        action = "download_img_with_thumb"
    elif action_name == 'file':
        action = "download_file"
    elif action_name == 'error':
        action = "download_error_list"

    if action:
        console = None if console == 'None' else console == 'True'
        down = downloader(action, console)

        eval("down.%s()" % action)