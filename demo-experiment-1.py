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
i+=2
print(mo)
print(i)    