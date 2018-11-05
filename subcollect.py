# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author: smelond
# blog: https://smelond.com

import argparse
from libs import start

if __name__ == '__main__':
    __version__ = "v.1.0 --- author: smelond"
    parser = argparse.ArgumentParser(description='子域名在线搜集')
    parser.add_argument('-V', '--version', help="version", action='version', version='%(prog)s ' + __version__)
    parser.add_argument('-u', dest="URL", type=str, help="subdomain", required=True)
    parser.add_argument('--proxy', dest='PROXY', help='proxy-server -> "socks5://127.0.0.1:1080"')
    args = parser.parse_args()
    start.main(args)
