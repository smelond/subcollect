# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author: smelond
# blog: https://smelond.com

from .public import *


# https://searchdns.netcraft.com/?restriction=site+contains&host=smelond.com
class excf:
    def __init__(self):
        self.headerparam = {
            "Cookie": "__utmz=257517449.1540019578.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=257517449; __utma=257517449.564081019.1540019578.1541420313.1541427346.15; netcraft_js_verification_challenge=djF8RW14YVdYQ1FqRE1veTdvMmpFSFRmN1pGZ0I1Yi9Ib2FmNEZ2ZmJCMjNvcnNCNXlrdGswUTJ3%0AejVCbWhMdE1SRXhsb1lPQ2xYSHQ5WApnVVNLTmxlMVhBPT0KfDE1NDE0MzI3NTI%3D%0A%7Cdfcb0405199776411521940b1836e38003d98644; netcraft_js_verification_response=9526a2a0297f051b0cacaab70a30e5a5096523de",
            "Connection": "keep-alive",
        }  # 存放cookie的字典

    def ssoup(self, url):
        li = []
        url = str(url).strip("*.")
        soup = setting.core.Reptilian()
        text = soup.REBsoup(url, self.headerparam)
        domain_html = text.find_all("a", attrs={"rel": "nofollow"})
        page = text.find_all("p", attrs={"align": "center"})
        page = "https://searchdns.netcraft.com" + str(page[-1].a['href']).replace("&amp;", "&").replace(" ", "+")
        for line in domain_html:
            li.append(str(line['href']).strip("http://").strip("/"))
        return li, page

    def get_domain(self, param):
        li = []
        domain, page = self.ssoup("https://searchdns.netcraft.com/?restriction=site+contains&host={}".format(param))
        for line in domain: li.append(line)
        try:
            for i in range(100):
                two_domain, page = self.ssoup(page)
                if page is None or two_domain is None: break
                for twoline in two_domain:
                    li.append(twoline)
        except:
            pass
        return list(set(li))
        # li = list(set(li))
        # for line in li:
        #     print(line)
        # print(len(li))
