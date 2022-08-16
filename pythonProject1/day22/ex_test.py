import requests
import json
url ="http://127.0.0.1:5000/content/2"
res = requests.post(url ,
                    json={"name":'nick', "views":10, "likes":100})
print(res)
print(res.json())