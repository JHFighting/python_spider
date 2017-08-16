# mysql 简单封装
# 
import pymysql

class Mysql_Handler:

    DB='db'
    USER='username'
    PASSWORD='password'
    PORT=3306
    HOST='localhost'
    CHARSET='utf8'

    connection = ""

    def __init__(self, host=HOST, port=PORT,user=USER,db=DB,passwd=PASSWORD,charset=CHARSET):
        Mysql_Handler.connect(self, host, port, user, db, passwd, charset)

    def connect(self, host=HOST, port=PORT,user=USER,db=DB,passwd=PASSWORD,charset=CHARSET):
        conn = pymysql.connect(host=host, port=port,user=user,db=db,passwd=passwd,charset=charset)
        self.connection = conn

    def insert(self, tableName, result):
        """
        插入一条数据
        :param tableName: 表名
        :param result: 数据, dict
        :return: False: 失败, True: 成功
        """
        if self.connection == '':
            print("Please connect first")
            return False
        cur = self.connection.cursor()
        keys = []
        values = []
        for key in result.keys():
            keys.append(key)
            values.append(result[key])

        try:
            sql = "insert into %s (%s) VALUES ('%s')"%(tableName, ",".join(keys), "','".join(values))
            cur.execute(sql)
            self.connection.commit()
            return True

        except Exception as e:
            print("insert error: %s"%(str(e)))
            return False

    def close():
        if self.connection:
            self.connection.close()
            self.connection = ""
