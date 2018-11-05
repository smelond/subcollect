# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author: smelond
# blog: https://smelond.com

import os
import random

from storage.my_sql import sdb
from libs import core

### mysql
mysql_switch = True
mysql_db = sdb(host="127.0.0.1",
               username="root",
               password="root",
               databases="test",
               port=3306)

### file output
files_output_switch = True
file_output = os.getcwd() + "/output"  # 默认文件输出位置

### socks5
socks5_switch = True
socks5 = "socks5://127.0.0.1:1081"  # 代理地址
socks5 = {
    'http': socks5,
    'https': socks5
}
### exec_file
li = []
f_list = os.listdir(os.getcwd() + "/sub_file/")
# f_list = os.listdir(os.getcwd())
for i in f_list:
    if os.path.splitext(i)[0] == "__init__" or os.path.splitext(i)[0] == "public":
        continue
    if os.path.splitext(i)[1] == '.py':
        li.append(str(i.split(".")[0]))
exec_file = li
### exec_file import
from sub_file import crt
from sub_file import netcraft
from sub_file import baidu


### Process number
process_number = 4  # 进程数量


### headers
def __random__():
    return str(random.randint(1, 223))


def __ua__():
    with open("UserAgent.txt", "r") as ua:
        return random.sample(ua.readlines(), 1)[0].strip("\n")


def header(reheader=None):
    _random_ = "%s.%s.%s.%s" % (__random__(), __random__(), __random__(), __random__())
    REQUEST_HEADER = {
        "User-Agent": "%s" % __ua__(),
        "X-Forwarded-For": "%s" % _random_,
        "CLIENT_IP": "%s" % _random_,
    }
    if reheader is not None:
        for k, v in reheader.items():
            REQUEST_HEADER[k] = v
    return REQUEST_HEADER
