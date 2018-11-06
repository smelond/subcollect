# subcollect 使用：
基于Python3
## 安装模块：
```bash
sudo pip install beautifulsoup4
sudo pip install requests
sudo pip install PyMySQL
```
``` bash
git clone https://github.com/smelond/subcollect
cd subcollect
vim setting.py   # 找到socks5修改为你自己的地址，或者将上面的socks5_switch = True修改为socks5_switch = False
python subcollect.py -u baidu.com
等待获取结果...
cd output
vim result_baidu.com.txt
```
结果图：
![Image text](https://smelond.com/image_upload/2018/11/20181105234951.png)

# 执行之前需要注意的几点：
这是工具使用的是socks5链接国外的网站进行在线查询，具体可以查看setting.py文件
如果直接执行脚本，netcraft是不会执行的，需要先打开netcraft网站，然后拿到cookie，将cookie写到self.headerparam = {} 这个字典里面，因为他过期的好像很快，像下面这样添加：
![Image text](https://smelond.com/image_upload/2018/11/20181105200704.png)

# 他是如何工作的：
目前我只加入了三个在线搜集子域名的网站，他们分别是crt、netcraft、baidu，当然还有很多可以在线搜集的网站，我这里只写了三个，你可以写更多的扩展到工具里面，使他变的更强大。
他是如何工作的？你可以查看链接：https://smelond.com/2018/11/05/subcollect子域名在线搜集
