import pandas  as pd
import csv
file=open("Prelogs.txt","r")
reader=file.readlines()
modified_reader=[]
for line in reader:
    modified_reader.append(line.strip())

prelogs_csv=open("Prelogs.csv","w")
prelogs_csv.write(" ")
prelogs_csv=open("Prelogs.csv","a")
for line in modified_reader:
    text=",".join(line.split())
    text=text+"\n"
    prelogs_csv.write(text)




df=csv.reader(open("Prelogs.csv","r"))
df=pd.DataFrame(df)
print(df)
df.to_excel('output.xlsx','Sheet 1',index=False)
prelogs_csv.close()
file.close()