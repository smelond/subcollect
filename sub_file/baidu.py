# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author: smelond
# blog: https://smelond.com

from .public import *


# http://www.baidu.com.cn/s?wd=site:smelond.com&cl=3&pn=10
class excf:
    def __init__(self):
        self.headerparam = {}  # 存放cookie的字典

    def ssoup(self, url):
        li = []
        soup = setting.core.Reptilian()
        text = soup.REBsoup(url, self.headerparam)
        domain_html = text.find_all("a", attrs={"class": "c-showurl"})
        for line in domain_html:
            line = str(line.string).strip("https://").strip("/ ")
            li.append(line)
        return li

    def get_domain(self, param):
        domain_list = []
        try:
            for i in range(50):
                i = i * 10
                domain = self.ssoup("https://www.baidu.com/s?wd=site:{}&cl=3&pn={}".format(param, i))
                if domain is None:
                    break
                for line in domain:
                    line = str(line).split("/")[0]
                    domain_list.append(line)
        except:
            pass
        return list(set(domain_list))
        # domain_list = list(set(domain_list))
        # for line in domain_list:
        #     print(line)
        # print(len(domain_list))
