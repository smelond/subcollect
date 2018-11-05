# /usr/bin/env python
# _*_ coding:utf-8 _*_
# author: smelond
# blog: https://smelond.com

import pymysql


class sdb:
    def __init__(self, **kwargs):
        self.host = kwargs['host']  # ip
        self.port = kwargs['port']  # 端口
        self.username = kwargs['username']  # 数据库用户名
        self.password = kwargs['password']  # 数据库密码
        self.databases = kwargs['databases']  # 连接的数据库
        self.sdb_connect()

    def sdb_connect(self):
        db = pymysql.connect(host=self.host,
                             port=int(self.port),
                             user=self.username,
                             password=self.password,
                             db=self.databases,
                             charset="utf8")
        return db

    def inserts(self, query):
        db = self.sdb_connect()
        cursor = db.cursor()
        try:
            cursor.execute(query)
            db.commit()
        except:
            db.rollback()
        db.close()

    def selects(self, query):
        db = self.sdb_connect()
        cursor = db.cursor()
        cursor.execute(query)  # 执行mysql命令
        data = cursor.fetchall()  # 获取返回结果
        db.commit()
        db.close()
        return data


# db = sdb(host="127.0.0.1", username="root", password="root", databases="test", port=3306)
# # # db.inserts("INSERT INTO shiyan(username, password) VALUES ('smelond','qweqwe')")
# print(db.selects("SELECT * FROM shiyan limit 0,1"))
