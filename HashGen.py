import pandas as pd
import time
import datetime
from requests import get

filename=input("Enter name of csv file: ")
event_name = input("Enter name of event: ")
year=input("Enter the year: ")
certificate = input("Enter name of certificate file: ")
#count = int(input("Enter the number of the first certificate: "))
count = get("http://cert-iiit.tk/count?format=json").json()['count']
dataset=pd.read_csv(filename);
emails = dataset['Email']

dataset = dataset.drop('Email', axis = 1)

details=dataset.iloc[:,1:].values

cert_id=[]
filenames = []
i=count
today = datetime.date.today().strftime('%d-%m-%Y')
date = []
for detail in details:
    
    detail[0]=str(detail[0])
    x=f"IIITV/STUD-GYMKHANA/CERT/{year}/{i:06}"
    fname = f"IIITV-STUD-GYMKHANA-CERT-{year}-{i}.pdf"
    i+=1
    filenames.append(fname)
    cert_id.append(x)
    date.append(today)
    

dataset['Certificate ID']=cert_id
dataset['Date'] = date
rollno = dataset['RollNo']
dataset = dataset.drop('RollNo', axis = 1)


dataset['RollNo']=rollno
dataset['Filename']=filenames
dataset['Email'] = emails
dataset.to_csv(f'{event_name}_{year}.csv',index=False)

print("HashGen done")
