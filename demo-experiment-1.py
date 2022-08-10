from tkinter.tix import DirTree
import pandas as pd
import xlsxwriter as xls
# pre_log=open("Prelogs.txt","r")
# print(pre_log)
workbook= "IP_mig_dt.xlsx"
df=pd.read_excel(workbook,"PRE")
#dataframe=pd.DataFrame()
mo=dict()
for i in range(0,len(df)):
    if df.iloc[i][0] != "END":
        if df.iloc[i][0]=='MO':
            mo[df.iloc[i+1][0]]=df.iloc[i+1][1]
            i+=1

    else:
        break
mo_refined=dict()
cell_chgrp=dict()
for j in range(i,len(df)):
    if df.iloc[j][0] in mo:
        mo_refined[df.iloc[j][0]]=df.iloc[j][1]
        cell_chgrp[df.iloc[j][1]]=list()

for j in range(i,len(df)):
    if df.iloc[j][1] in mo_refined.values():
        temp=df.iloc[j][2]
        cell_chgrp[df.iloc[j][1]].append(temp)

# print(mo_refined)
print(len(mo_refined))
# print(cell_chgrp)
print(len(cell_chgrp))
old_tg=list(mo_refined.keys())

# getting the list of old tg from pre
for j in range(len(old_tg)):
    temp=old_tg[j]
    temp=temp[6:]
    old_tg[j]=temp

print(old_tg)

