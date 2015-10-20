# -*- coding: utf-8 -*-  
#---------------------------------------  
#   程序：连接netezza数据库
#   版本：0.1 
#   作者：Saber Wu
#   日期：
#   语言：Python 3.4 
#   操作：
#   功能： 
#---------------------------------------

import pyodbc

conn = pyodbc.connect(dsn='')
curs = conn.cursor()
curs.execute("select * from dual")

rows = curs.fetchall()
for row in rows:
    print (row)

curs.close()
conn.close()