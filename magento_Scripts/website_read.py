import json
import requests
API_URL = 'http://83.169.11.147/magento214Demo/rest/V1/store/storeConfigs'
TOKEN = 'wbinpahujdaum9bhatgorg1fjds8g69h'
headers = {'Accept':'*/*','Content-Type':'applicaton/json','Authorization':'Bearer %s'%TOKEN}
res = requests.get(API_URL,headers = headers,verify=False)
print res.text
print res.status_code
print res.reason
