import json
import requests
from php import Php
#API_URL = 'http://192.168.0.151/magento213/rest/V1/orders/68'
#API_URL = 'http://m2zc5.test.dev.zococity.es/rest/V1/orders/27946'	
#TOKEN = '02vfb8k3da4hriip2d58toyely6s0166'

#API_URL = 'http://192.168.0.149/Ankita/magentoS2/rest/V1/orders/47'
#TOKEN = 'duwavxgusj64kyjne65mo9g6p4sbu1gk' 
#API_URL = 'http://erptest.mage2.emiprotechnologies.com/rest/V1/orders/63'

#API_URL = 'http://erptest.mage2.emiprotechnologies.com/rest/V1/shipments?'
#filters = {'searchCriteria':{'filterGroups':[{'filters':[{'field':'entity_id','value':"60",'condition_type':'eq'}]}]}}
#qs = Php.http_build_query(filters)
#url = API_URL+qs
filters = {'searchCriteria':{'filterGroups':[{'filters':[{'field':'entity_type_id','value':-1,'condition_type':'gt'}]}]}}
qs = Php.http_build_query(filters)
#API_URL="http://192.168.0.43/Deep/Customoption/MagentoCOM219/rest/V1/orders/4"
#API_URL="http://192.168.0.43/Deep/Customoption/MagentoCOM219/rest/V1/customers/1"
#TOKEN='hmb06qgt7xcmyc5joreap32nq4j65drt'
TOKEN = "b1skq9lxygq39heynciw221vsjip0skf"
API_URL = "http://192.168.0.38/angel/Poolspot/rest/V1/products/attribute-sets/sets/list?%s"%(qs)
headers = {'Accept':'*/*','Content-Type':'applicaton/json','Authorization':'Bearer %s'%TOKEN}
res = requests.get(API_URL,headers = headers,verify=False)
print API_URL
print res.text
print res.status_code
print res.reason
