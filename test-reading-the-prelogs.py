import re
file=open("Prelogs.txt")
reader=file.readlines()
modified_reader=[]
for line in reader:
    modified_reader.append(line.strip())
pre_stg=[]
pre_sector=[]
pre_Rsite=[]
for i in range(0,len(modified_reader)):
    line=modified_reader[i].split()
    if "END" in line:
        break
    else:
        if "MO" in line:
            continue
        
        elif len([x for x in line if re.findall("\ARXSTG",x)])>0:
            pre_stg.append(int(line[0][6:]))
            pre_sector.append(line[1])
            pre_Rsite.append(line[2])
        else:
            continue
mo=dict() # contains dictionary Sector: Rxstg from pre
for j in range(0,len(pre_sector)):
    mo[pre_sector[j]]=pre_stg[j]

rsite=dict()
for j in range(0,len(pre_sector)):
    rsite[pre_sector[j]]=pre_Rsite[j]
chgr=dict()
for j in range(0,len(pre_sector)):
    chgr[pre_sector[j]]=list()

for j in range(i,len(modified_reader)):
    line=modified_reader[j].split()
    if len(line)>0 and line[0] in mo:
        chgr[line[0]].append(line[1])
    elif len(line)>2 and line[1] in mo:
        chgr[line[1]].append(line[2])
    else:
        continue

print(rsite)
file.close()