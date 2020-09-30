import pandas as pd
import hashlib as hl
import base64
import time
import datetime
import urllib

filename=input("Enter name of csv file: ")
event_name = input("Enter name of event: ")
year=input("Enter the year: ")
certificate = input("Enter name of certificate file: ")
count = int(input("Enter the number of the first certificate: "))
dataset=pd.read_csv(filename);


details=dataset.iloc[:,1:].values

hash1=[]
filename = []
i=count
today = datetime.date.today().strftime('%d-%m-%Y')
date = []
for detail in details:

    detail[0]=str(detail[0])
    x=f"IIITV/STUD-GYMKHANA/CERT/{year}/{i:05}"
    #x=x.encode(encoding='UTF-8',errors='strict')
    #hash_object=hl.md5(x)
    #hash1.append(hash_object.hexdigest())
   # fname = detail[0]+ '-' + str(time.time()).replace('.', '-')
    fname = f"IIITV-STUD-GYMKHANA-CERT-{year}-{i}.pdf"
    i+=1
    filename.append(fname)
    #print(fname)
    hash1.append(x)
    date.append(today)
    

dataset['Certificate ID']=hash1
dataset['Date'] = date
x=dataset.iloc[:,[1]].values
del dataset['RollNo']


dataset['RollNo']=x
dataset['Filename']=filename
dataset.to_csv(f'{event_name}_{year}.csv',index=False)

print("HashGen done")
    
