import re
file=open("Prelogs.txt")
reader=file.readlines()
modified_reader=[]
for line in reader:
    modified_reader.append(line.strip())
for i in range(0,modified_reader):
    line=modified_reader.split()
    if "END" in line:
        break
    else:
        if "MO" in line:
            continue
        
        elif 
        else:
            continue
print(modified_reader)
file.close()