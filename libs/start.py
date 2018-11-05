# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author: smelond
# blog: https://smelond.com


from multiprocessing import Pool
import os, random, sys, datetime, socket
import setting


class main:
    def __init__(self, args):
        self.url = args.URL
        self.proxy = args.PROXY
        self.start()

    def load_script(self, name, min_time):
        eval_script = eval("setting.{}.excf()".format(name))
        result_list = eval_script.get_domain(self.url)
        with open(min_time, "a") as files:
            for line in result_list:
                files.write(line + "\n")

    def start(self):  # 启动多进程
        domain_list = []
        min_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # 当前天，时，分，秒
        p = Pool(int(setting.process_number))  # 获取进程数量
        file_list = setting.exec_file  # 获取文件
        for i in range(len(file_list)):
            p.apply_async(self.load_script, args=(file_list[i], min_time))
        p.close()
        p.join()

        with open(min_time, "r") as files:
            for line in files.readlines():
                line = line.strip("\n")
                if line.startswith(".") or line.startswith("*"): continue
                domain_list.append(line)
        os.remove(min_time)  # 删除文件
        domain_list = list(set(domain_list))
        with open("output/all_" + self.url, "a") as file:
            for line in domain_list:
                file.write(line + "\n")
        p = Pool(400)
        for i in range(len(domain_list)):
            p.apply_async(self.screens, args=(domain_list[i],))
        p.close()
        p.join()

    def screens(self, domain):
        addr = socket.getaddrinfo(domain, 'http')
        if addr[0][4][0]:
            with open("output/result_" + self.url + ".txt", "a") as file:
                file.write(domain + "\t" + addr[0][4][0] + "\n")
            print(domain + "\t" + addr[0][4][0])
