
import json
import requests
API_URL = 'http://m2zc2.test.dev.zococity.es/rest/V1/products/attribute-sets/groups/list?searchCriteria[filterGroups][0][filters][0][field]=attribute_set_id&searchCriteria[filterGroups][0][filters][0][condition_type]=eq&searchCriteria[filterGroups][0][filters][0][value]=17&'
TOKEN = 'w81r5ue36wbjcwrimads2t44vrw2crey'
headers = {'Accept':'*/*','Content-Type':'applicaton/json','Authorization':'Bearer %s'%TOKEN}
res = requests.get(API_URL,headers = headers,verify=False)
print res.text
print res.status_code
print res.reason



API_URL = 'http://m2zc2.test.dev.zococity.es/rest/V1/attribute'
TOKEN = 'w81r5ue36wbjcwrimads2t44vrw2crey'
data = {'attribute_set_id':4}
headers = {'Accept':'*/*','Content-Type':'applicaton/json','Authorization':'Bearer %s'%TOKEN}
res = requests.post(API_URL,headers = headers,data=json.dumps(data),verify=False)
print res.text
print res.status_code
print res.reason
"""

import json
import requests
API_URL = 'http://192.168.0.151/magento213/rest/V1/products/attribute-sets/groups/list?searchCriteria[filterGroups][0][filters][0][field]=attribute_set_id&searchCriteria[filterGroups][0][filters][0][condition_type]=eq&searchCriteria[filterGroups][0][filters][0][value]=7&'
TOKEN = '0vkwajywx49ckjdhuv6uvxi961riusrx'
headers = {'Accept':'*/*','Content-Type':'applicaton/json','Authorization':'Bearer %s'%TOKEN}
res = requests.get(API_URL,headers = headers,verify=False)
print res.text
print res.status_code
print res.reason


data = {
          'attribute_set_id':10,
       }
API_URL = 'http://192.168.0.151/magento213/rest/V1/attribute'
TOKEN = '0vkwajywx49ckjdhuv6uvxi961riusrx'
headers = {'Accept':'*/*','Content-Type':'applicaton/json','Authorization':'Bearer %s'%TOKEN}
res = requests.post(API_URL,headers = headers,data=json.dumps(data),verify=False)
print res.text
print res.status_code
print res.reason
"""
