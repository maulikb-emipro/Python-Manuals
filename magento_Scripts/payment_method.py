import json
import requests

API_URL = 'http://erptest.mage2.emiprotechnologies.com/V1/paymentmethod'
TOKEN = 'duwavxgusj64kyjne65mo9g6p4sbu1gk'
headers = {'Accept':'*/*','Content-Type':'application/json','Authorization':'Bearer %s'%TOKEN}
res = requests.get(API_URL,headers=headers,verify=False)
print res.text
print res.status_code
print res.ok
