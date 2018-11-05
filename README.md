# subcollect 使用：

``` bash
git clone https://github.com/smelond/subcollect
cd subcollect
python subcollect.py -u baidu.com
等待获取结果...
cd output   # 这里可以看到返回的子域名
vim result_baidu.com.txt
```
搜集子域名的网站是crt、netcraft、baidu，当然还有很多可以在线搜集的网站
# 执行之前需要注意的一点：
需要注意一点的是，如果直接执行脚本，netcraft是不会执行的，需要先打开netcraft网站，然后拿到cookie，将cookie写到self.headerparam = {} 这个字典里面，因为他过期的好像很快，像下面这样添加：
https://smelond.com/image_upload/2018/11/20181105200704.png
