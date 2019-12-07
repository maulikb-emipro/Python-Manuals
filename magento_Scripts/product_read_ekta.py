
import json
import requests
API_URL = 'http://192.168.0.151/magento213/rest/V1/products'
TOKEN = 'jaetl6rrdq9mc50s5kcrypx10eb0nsoc'
headers = {'Accept':'*/*','Content-Type':'applicaton/json','Authorization':'Bearer %s'%TOKEN}

API_URL = 'http://erptest.mage2.emiprotechnologies.com/rest/V1/products?searchCriteria[filterGroups][0][filters][0][value]=2018-10-17%2010%3A29%3A20&searchCriteria[filterGroups][0][filters][0][condition_type]=to&searchCriteria[filterGroups][0][filters][0][field]=updated_at&searchCriteria[currentPage]=1&searchCriteria[pageSize]=200'


API_URL = "http://erptest.mage2.emiprotechnologies.com/rest/V1/products?searchCriteria[filterGroups][0][filters][0][value]=2018-10-17%2010%3A29%3A20&searchCriteria[filterGroups][0][filters][0][condition_type]=to&searchCriteria[filterGroups][0][filters][0][field]=updated_at"

API_URL = "http://erptest.mage2.emiprotechnologies.com/rest/V1/products?searchCriteria[currentPage]=1&searchCriteria[filterGroups][1][filters][0][value]=2018-10-17%2011%3A38%3A56&searchCriteria[filterGroups][1][filters][0][field]=updated_at&searchCriteria[filterGroups][1][filters][0][condition_type]=to&searchCriteria[filterGroups][0][filters][0][value]=configurable&searchCriteria[filterGroups][0][filters][0][field]=type_id&searchCriteria[filterGroups][0][filters][0][condition_type]=eq&searchCriteria[pageSize]=200&"
#res = requests.post(API_URL,headers = headers,verify=False)
#res = requests.post(API_URL, data.get(body), headers = headers,verify=False)
res = requests.get(API_URL,headers=headers)
#print res.text
print res.json()
print len(res.json().get('items'))
print res.status_code
print res.reason





