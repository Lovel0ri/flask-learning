# @Time: 2022/9/14 0:09
# @Author: 李树斌
# @File : DBcm.py
# @Software :PyCharm

import mysql.connector
class UseDatabase:
    def __init__(self,config:dict)-> None:
        #config参数的值赋给一个名为”configuration"的属性
        self.configuration = config

    def __enter__(self)->'cursor':
        self.conn = mysql.connector.connect(**dbconfig)
        self.cursor = conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb)->None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

