import re
import pandas as pd

file=open("Prelogs.txt","r")
pre_reader=file.readlines()
modified_pre_reader=[] #n
for line in pre_reader:
    modified_pre_reader.append(line.strip())

del pre_reader



for i in range(0,len(modified_pre_reader)):
    if len(re.findall("\AEND",modified_pre_reader[i])):
        break

pre_stg_dict=dict()     # dictionary cell-input/sector:stg
pre_chgr_dict=dict()    # dictionary cell-input/sector:chgr
pre_stg_rsite=dict()    # dictionary cell_input/sector:rsite
for j in range(i, len(modified_pre_reader)):
    line=modified_pre_reader[j].split()
    if len(re.findall("\ARXSTG",modified_pre_reader[j]))>0:
        pre_stg_dict[line[1]]=line[0]
        pre_chgr_dict[line[1]]=list() 
        pre_chgr_dict[line[1]].append(line[2])
    
    elif len(line)>0 and modified_pre_reader[j].split()[0] in pre_chgr_dict:
        pre_chgr_dict[line[0]].append(line[1])
for j in range(0,i+1):
    line=modified_pre_reader[j].split()
    if len(re.findall("\ARXSTG",modified_pre_reader[j]))>0 and line[1] in pre_chgr_dict:
        pre_stg_rsite[line[1]]=line[2]

tg_list=list(pre_stg_dict.values())         # getting the list of all the prelog tg
rsite_list=list(pre_stg_rsite.values())     # getting the list of all the prelog rsite
cell_input_list=list(pre_stg_dict.keys())   # getting the list of all cell-input/sectors

for j in range(0,len(tg_list)):
    tg_list[j]=tg_list[j].lower()


file=open("Post_logs.txt","r")
post_reader=file.readlines()
modified_post_reader=[]

for line in post_reader:
    modified_post_reader.append(line.strip())


post_tg=[]

for i in range(0,len(modified_post_reader)):
    if len(re.findall("\ARXSTG",modified_post_reader[i]))>0 or len(re.findall("\ARXOTG",modified_post_reader[i]))>0:
        line=modified_post_reader[i].split()
        post_tg.append(int(line[0][6:]))

new_tg=[]   # new tg to be filld in the coloumn for new tg

i=0
size=len(tg_list)

while (len(new_tg)<size):
    if i not in post_tg and i<=8190:
        new_tg.append(i)
    i=i+1

cell_input=[]
chgr=[]
rsite=[]
newtg=[]
oldtg=[]
new_tg_defination_in_destination_bsc=[]
chgr_allocation_in_destination_bsc=[]
tg_deblock_iu_destination_bsc_rxesi=[]
tg_deblock_iu_destination_bsc_rxble=[]
cell_active_in_destination_bsc=[]
cell_halte_in_source_bsc=[]
tg_block_source_bsc_rxbli=[]
tg_block_source_bsc_rxese=[]



pre_chgr_list=list(pre_chgr_dict.values())
for j in range(0,len(pre_chgr_list)):
    for k in range(0,len(pre_chgr_list[j])):
        cell_input.append(cell_input_list[j])
        chgr.append(pre_chgr_list[j][k])
        rsite.append(rsite_list[j])
        newtg.append(new_tg[j])
        oldtg.append(int(tg_list[j][6:]))
        if k==0:
            temp1=f"rxmoi:mo={tg_list[j]},Sector={rsite_list[j][0:6]}_{rsite_list[j][6:]},RSITE={rsite_list[j]};"
            new_tg_defination_in_destination_bsc.append(temp1)
            
            temp2=f"rxesi:mo={tg_list[j]}"
            tg_deblock_iu_destination_bsc_rxesi.append(temp2)

            temp3=f"rxble:mo={tg_list[j]}"
            tg_deblock_iu_destination_bsc_rxble.append(temp3)

        else:
            temp1=""
            new_tg_defination_in_destination_bsc.append(temp1)

            temp2=""
            tg_deblock_iu_destination_bsc_rxesi.append(temp2)

            temp3=""
            tg_deblock_iu_destination_bsc_rxble.append(temp3)
        
        temp2=f"rxtci:mo={tg_list[j]},cell={cell_input_list[j]},chgr={pre_chgr_list[j][k]};"
        chgr_allocation_in_destination_bsc.append(temp2)

        temp3=f"rlstc:cell={cell_input_list[j]},chgr={pre_chgr_list[j][k]},state=active;"
        cell_active_in_destination_bsc.append(temp3)

        temp4=f"rlstc:cell={cell_input_list[j]},chgr={pre_chgr_list[j][k]},state=halted;"
        cell_halte_in_source_bsc.append(temp4)
        
        temp5=f"rxbli:mo={tg_list[j]}"
        tg_block_source_bsc_rxbli.append(temp5)

        temp6=f"rxese:mo={tg_list[j]}"
        tg_block_source_bsc_rxese.append(temp6)

pd.set_option('display.max_columns', None)
dataframe_dictionary={"CELL_INPUT":cell_input,"CHGR":chgr,"RSITE":rsite,"NEW TG":newtg,"OLD TG":oldtg,"NEW_TG_defination_in_destination_bsc":new_tg_defination_in_destination_bsc,"chgr_allocation in destination bsc":chgr_allocation_in_destination_bsc,"tg deblock iu destination bsc":tg_deblock_iu_destination_bsc_rxesi,"tg deblock iu destination bsc":tg_deblock_iu_destination_bsc_rxble,"cell active in destination bsc":cell_active_in_destination_bsc,"cell halte in source bsc":cell_halte_in_source_bsc,"TG block in source BSC":tg_block_source_bsc_rxbli,"TG block in source BSC":tg_block_source_bsc_rxese}
df=pd.DataFrame(dataframe_dictionary)

# print("\nlength of cell input: ",len(cell_input))
# print("\nlength of chgr: ",len(chgr))
# print("\nlength of rsite: ",len(rsite))
# print("\nlength of newtg: ",len(newtg))
# print("\nlength of oldtg: ",len(oldtg))
# print("\nlength of new_tg_defination_in_destination_bsc: ",len(new_tg_defination_in_destination_bsc))
# print("\nlength of chgr_allocation_in_destination_bsc: ",len(chgr_allocation_in_destination_bsc))
# print("\nlength of tg_deblock_iu_destination_bsc_rxesi: ",len(tg_deblock_iu_destination_bsc_rxesi))
# print("\nlength of tg_deblock_iu_destination_bsc_rxble: ",len(tg_deblock_iu_destination_bsc_rxble))
# print("\nlength of cell_active_in_destination_bsc: ",len(cell_active_in_destination_bsc))
# print("\nlength of cell_halte_in_source_bsc: ",len(cell_halte_in_source_bsc))
# print("\nlength of tg_block_source_bsc_rxbli: ",len(tg_block_source_bsc_rxbli))
# print("\nlength of tg_block_source_bsc_rxese: ",len(tg_block_source_bsc_rxese))

# print("\n length of rsite_list: ",len(rsite))
print(df.head())
file.close()