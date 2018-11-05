# subcollect 使用：

``` bash
git clone https://github.com/smelond/subcollect
cd subcollect
python subcollect.py -u baidu.com
等待获取结果...
cd output
vim result_baidu.com.txt
```
结果图：
![Image text](https://smelond.com/image_upload/2018/11/20181105234951.png)

# 执行之前需要注意的一点：
需要注意一点的是，如果直接执行脚本，netcraft是不会执行的，需要先打开netcraft网站，然后拿到cookie，将cookie写到self.headerparam = {} 这个字典里面，因为他过期的好像很快，像下面这样添加：
![Image text](https://smelond.com/image_upload/2018/11/20181105200704.png)

# 他是如何工作的：
目前我只加入了三个在线搜集子域名的网站，他们分别是crt、netcraft、baidu，当然还有很多可以在线搜集的网站，我这里只写了三个，你可以写更多的扩展到工具里面，使他变的更强大。
他是如何工作的？你可以查看链接：https://smelond.com/2018/11/05/subcollect子域名在线搜集
