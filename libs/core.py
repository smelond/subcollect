# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author: smelond
# blog: https://smelond.com


from bs4 import BeautifulSoup
import requests
import sys

import setting


class Reptilian:
    def __init__(self):
        pass

    def REBsoup(self, url, reheader):  # 请求url地址获取内容
        print(url)
        # s = requests.Session()
        result_content = requests.get(
            url, headers=setting.header(reheader), proxies=self.issocks())
        if int(result_content.status_code) < 400:
            result_content.encoding = "utf8"
            soup = BeautifulSoup(str(result_content.text), 'html.parser')
            return soup
        return "The network is not smooth..."

    def issocks(self):
        if setting.socks5_switch:
            return setting.socks5
        return None
