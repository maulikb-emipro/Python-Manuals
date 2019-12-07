import json
import requests
data = {
  "category": {
    "name": "Back pack",
  }
}
API_URL = 'http://p236400.mittwaldserver.info/magento216/rest/V1/categories/6'
TOKEN = 'g85930oxw74lqrwu51v9pff3ofa7y2af'
headers = {'Accept':'*/*','Content-Type':'applicaton/json','Authorization':'Bearer %s'%TOKEN}
res = requests.get(API_URL,headers = headers,verify=False)
print res.text
print res.status_code
print res.reason


