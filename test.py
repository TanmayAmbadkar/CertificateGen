'''
from requests import get, post

data = {
    'username': 'tanmay4',
    'password' : 'sarutata',
    'first_name' : 'Tanmay',
    'last_name' : 'Ambadkar',
    'email' : 'tanmay.ambadkar@gmail.com'
    
}
headers = { 'Authorization' : 'Token 81cd6921697b124c3178328b482193845c1c9cd7'}

url = "http://localhost:8000/signup"
r = post(url, data=data)
print(r.text)
'''
from requests import get, post

data = {
    'username': 'username2',
    'password': 'abcd1234',
    'id': 1101,
    'quantity' : 20,
    
}
headers = { 'Authorization' : 'Token 1457df3b259c9b9de3c2adf45a3b602ef17f0b33'}

url = "http://localhost:8000/family/buy"
r = get(url, headers=headers, data=data)
print(r.text)
