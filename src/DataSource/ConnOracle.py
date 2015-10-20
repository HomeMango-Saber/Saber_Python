# -*- coding: utf-8 -*-  
#---------------------------------------  
#   程序：连接oracle数据库
#   版本：0.1 
#   作者：Saber Wu
#   日期：
#   语言：Python 3.4 
#   操作：
#   功能： 
#---------------------------------------

import cx_Oracle;

conn = cx_Oracle.connect("")
curs  = conn.cursor()
# curs.execute("select * from t_ddw_dmn_date")
#
# rows = curs.fetchall()
# for row in rows:
#     print (row)


print(conn.version)


curs.close()
conn.close()

