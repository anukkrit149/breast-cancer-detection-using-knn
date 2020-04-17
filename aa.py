import requests

url = 'http://project.wisekreator.com/nn/api.php'
myobj = {'userId': 1312,'packages':"a,b,c,d"}

x = requests.post(url, data = myobj)

print(x.text)