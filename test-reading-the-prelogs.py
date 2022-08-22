import re
def func1():
    file=open("Prelogs.txt","r")
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
                pre_stg.append(line[0])
                pre_sector.append(line[1])
                pre_Rsite.append(line[2])
            else:
                continue
    mo=dict() # contains dictionary Sector: Rxstg from pre
    pre_stg_dict_with_num=dict()
    for j in range(0,len(pre_stg)):
        pre_stg_dict_with_num[pre_stg[j]]=int(pre_stg[j][6:])

    for j in range(0,len(pre_sector)):
        mo[pre_sector[j]]=pre_stg_dict_with_num.get(pre_stg[j])

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
    # for key in chgr:
    #     if len(chgr.get(key))==0:
    #         chgr.pop(key)
    #         rsite.pop(key)
    #         mo.pop(key)
    # print(mo)

    file=open("Post_logs.txt","r")
    reader2=file.readlines()
    modified_reader2=[]
    for line in reader2:
        modified_reader2.append(line.strip())

    post_tg=[]
    for j in range(0,len(modified_reader2)):
        if len(re.findall("\ARXSTG",modified_reader2[j]))>0 or len(re.findall("\ARXOTG",modified_reader2[j]))>0:
            line=modified_reader2[j].split()
            post_tg.append(line[0][6:])
    new_tg=[]
    i=0
    while(len(new_tg)<=len(pre_sector)) or i<=8190:
        if i not in post_tg:
            new_tg.append(i)
        else:
            continue
        i+=1
    print(len(pre_Rsite))
    print(len(new_tg))

    for j in range(0,len(pre_stg)):
        pre_stg[j]=pre_stg[j].lower()

    #print(mo)
    #print(chgr)
    file.close()


func1()
