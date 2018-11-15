import numpy as np
import xlrd
import os
#**************************************************************
name=input('Input the Excel file name:')
data=xlrd.open_workbook(os.getcwd()+'/'+str(name)+'.xlsx')
table=data.sheet_by_index(0)
s=[]
for i in range(2,int(table.nrows)):
    b=''
    for a in range(int(table.ncols)):
        b+=str(table.row_values(i)[a])
    s.append(b)
file=open(os.getcwd()+'/'+str(name)+'.fasta','w')
for j in range(int(table.nrows)-2):
    file.write(str(s[j])+'\n')
file.close()
