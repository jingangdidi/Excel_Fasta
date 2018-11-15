import numpy as np
import xlrd
import os
#**************************************************************
name=input('Input the Excel file name:')
data=xlrd.open_workbook(os.getcwd()+'/'+str(name)+'.xlsx') #获取‘生成序列谱文本文件.py’的路径
table=data.sheet_by_index(0)
s=[] #将excel数据每行作为一个元素写入列表中
for i in range(2,int(table.nrows)): #第一行为标题行，排除
    b=''
    for a in range(int(table.ncols)): #每行元素合并为一个元素
        b+=str(table.row_values(i)[a])
    s.append(b) #将每行元素写入列表
file=open(os.getcwd()+'/'+str(name)+'.fasta','w')
for j in range(int(table.nrows)-2): #每行元素写入fasta文本文件
    file.write(str(s[j])+'\n')
file.close()