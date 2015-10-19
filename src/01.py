# -*- coding: utf-8 -*-  
#---------------------------------------  
#   程序：Python语法练习01
#   版本：0.1 
#   作者：Saber Wu
#   日期：
#   语言：Python 3.4 
#   操作：
#   功能： 
#---------------------------------------

import sys
def Main():
    array=[1,2,3]
    print (array[0] )
    array[0]='a'
    print (array )
    # #输出['a',2,3]
    L=[123,'spam',1.23]
    # #输出大小
    print (len(L) )
    print (L[0])
    print (L[:-1])   #不包含最后一个
    print (L+[4,5,6]) #重新拼接一个新的列表

    test=['never',1,2,'yes',1,'no','maybe']
    print (test[0:3])#包括test[0],不包括test[3]
    print (test[0:6:2])#包括test[0],不包括test[6],而且步长为2
    print (test[:-1])#包括开始，不包括最后一个
    print (test[-3:])#抽取最后3个
if __name__=="__main__":
    Main()