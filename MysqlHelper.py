# coding=utf-8'
import pymysql
class MysqlHelper:
    def __init__(self,host,db,user,pwd,port=3306,charset="utf-8"):
        self.host=host
        self.port=port
        self.db=db
        self.user=user
        self.pwd=pwd
        self.charset=charset

    # 连接数据库
    def connect(self):
        self.conn=pymysql.connect(host=self.host, port=self.port,
            user=self.user, passwd=self.pwd,db=self.db)
        self.cursor=self.conn.cursor()

    # 关闭连接
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 对数据库做操作
    def cud(self,sql,params=()):
        try:
            # self.open()
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as err:
            print(err)

    # 获取查询所有结果
    def all(self,sql,params=()):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.close()
            return result
        except Exception as err:
            print(err)

