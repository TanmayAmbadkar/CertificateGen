import pandas as pd
import hashlib as hl
import base64
import time

filename=input("Enter name of csv file: ")
dataset=pd.read_csv(filename);

event_name=input("Enter name of your event: ")
year=input("Enter the year: ")

details=dataset.iloc[:,1:].values

hash1=[]
filename = []
i=0
for detail in details:

    detail[0]=str(detail[0])
    s="-".join(detail)
    x="{}-{}-{}".format(event_name,year,s)
    x = x.lower()
    #x=x.encode(encoding='UTF-8',errors='strict')
    #hash_object=hl.md5(x)
    #hash1.append(hash_object.hexdigest())
   # fname = detail[0]+ '-' + str(time.time()).replace('.', '-')
    fname = f"{x}.pdf"
    i+=1
    filename.append(fname)
    #print(fname)
    hash1.append(x)
    

dataset['Hash']=hash1
x=dataset.iloc[:,[1]].values
del dataset['RollNo']


dataset['RollNo']=x
dataset['Filename']=filename
dataset.to_csv('generated.csv',index=False)

print("HashGen done")
    
