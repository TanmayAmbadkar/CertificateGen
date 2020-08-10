import pandas as pd
import hashlib as hl
import base64

filename=input("Enter name of csv file: ")
dataset=pd.read_csv(filename);

event_name=input("Enter name of your event: ")
year=input("Enter the year: ")

details=dataset.iloc[:,1:].values

for i in range(0,len(details)):
    details[i][0]=int(details[i][0])
hash1=[]
i=0
for detail in details:
    if(detail[1]=='-'):
        dataset['Sub Event Name'][i]=detail[2]
    detail[0]=str(detail[0])
    detail[1]="".join(detail[1].split())
    i+=1
    s="/".join(detail)
    x="{}/{}/{}".format(event_name[0:2],year[2:],s)
    #print(x)
    x=x.encode(encoding='UTF-8',errors='strict')
    hash_object=hl.md5(x)
    hash1.append(hash_object.hexdigest())
    

dataset['Hash']=hash1
x=dataset.iloc[:,[1]].values
del dataset['RollNo']
del dataset['Position']
dataset['RollNo']=x
dataset.to_csv('generated.csv',index=False)

print("HashGen done")
    
