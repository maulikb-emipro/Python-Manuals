import json
import requests
API_URL = 'http://m2zc5.test.dev.zococity.es/rest/V1/customers/26691'
TOKEN = '02vfb8k3da4hriip2d58toyely6s0166'
headers = {'Accept':'*/*','Content-Type':'applicaton/json','Authorization':'Bearer %s'%TOKEN}
res = requests.get(API_URL,headers = headers,verify=False)
print res.text
print res.status_code
print res.reason
