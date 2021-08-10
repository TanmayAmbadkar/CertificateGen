from requests import get, post

# data = {
    # 'event': 'Gymkhana',
    # 'year' : '2019',
    # 'token' : "e56ee03623b2eb9e332e1244079ae0838eb6f02a"
# }

# files = {
    # 'image': open('club.jpg', 'rb'),
    # 'csv': open('kreiva.csv', 'rb')
# }
# url = "http://localhost:8000/generate"
# r = post(url, data=data, files=files)
# print(r.text)

data = {
    'id': 22,
    'token' : "e56ee03623b2eb9e332e1244079ae0838eb6f02a"
}

files = {
    'zip': open('certificate-9-8-2021.zip', 'rb')
}
url = "http://localhost:8000/upload"
r = post(url, data=data, files=files)
print(r.text)

# data = {
    # 'username': 'tanmay',
    # 'password' : 'sarutata',
# }

# files = {
    # 'image': open('club.jpg', 'rb'),
    # 'csv': open('kreiva.csv', 'rb')
# }
# url = "http://localhost:8000/login"
# r = post(url, data=data)
# print(r.text)
