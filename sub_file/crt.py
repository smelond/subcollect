# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author: smelond
# blog: https://smelond.com

from .public import *


# https://crt.sh/?q=%.smelond.com
class excf:
    def __init__(self):
        self.headerparam = {}  # 存放cookie的字典

    def ssoup(self, url):
        url = str(url).strip("*.")
        li = []
        li_er = []
        soup = setting.core.Reptilian()
        text = soup.REBsoup("https://crt.sh/?q=%.{}".format(url), self.headerparam)
        text = text.find_all("td")
        for line in text:
            if url not in str(line) or len(str(line)) > 300 or "Identity LIKE" in str(line):
                continue
            new_domain = str(line).strip("<td>").strip("</td>")
            if "*." not in new_domain or new_domain == "*.%s" % url:
                if new_domain == "*.%s" % url:
                    li.append(new_domain.replace("*.", ""))
                    continue  # 排除*.smelond.com
                li.append(new_domain)  # 如果删除td标签后没有*. 则加入列表 例如param1 = *.smelond.com www.smelond.com
                continue
            li_er.append(new_domain)
        return list(set(li)), list(set(li_er))

    def get_domain(self, param):
        domain, wildcard = self.ssoup(param)
        for thline in wildcard:  # 进行三次筛选，可以获取到
            thlevel_domain, thlevel_wildcard = self.ssoup(thline)
            for foline in thlevel_wildcard:
                folevel_domain, folevel_wildcard = self.ssoup(foline)
                for line in folevel_domain:
                    domain.append(line)
            for line in thlevel_domain:
                domain.append(line)
        # domain = list(set(domain))
        # for line in domain:
        #     print(line)
        # print(len(domain))
        return list(set(domain))
