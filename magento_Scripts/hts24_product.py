
import json
import requests
# API_URL = 'http://192.168.0.151/magento213/rest/V1/products'
TOKEN = 'g7ayvu42rz1gqvohjqyhymthnt1t31o3'
headers = {'Accept':'*/*', 'Content-Type':'applicaton/json', 'Authorization':'Bearer %s' % TOKEN}

# API_URL = 'http://erptest.mage2.emiprotechnologies.com/rest/V1/products?searchCriteria[filterGroups][0][filters][0][value]=2018-10-17%2010%3A29%3A20&searchCriteria[filterGroups][0][filters][0][condition_type]=to&searchCriteria[filterGroups][0][filters][0][field]=updated_at&searchCriteria[currentPage]=1&searchCriteria[pageSize]=200'

# API_URL = "http://erptest.mage2.emiprotechnologies.com/rest/V1/products?searchCriteria[filterGroups][0][filters][0][value]=2018-10-17%2010%3A29%3A20&searchCriteria[filterGroups][0][filters][0][condition_type]=to&searchCriteria[filterGroups][0][filters][0][field]=updated_at"
temp = 1
while True:
    API_URL = "https://www.hts24.de/rest/V1/products?searchCriteria[filterGroups][1][filters][0][value]=2019-05-15%2011%3A38%3A56&searchCriteria[filterGroups][1][filters][0][field]=updated_at&searchCriteria[filterGroups][1][filters][0][condition_type]=to&searchCriteria[filterGroups][0][filters][0][value]=simple&searchCriteria[filterGroups][0][filters][0][field]=type_id&searchCriteria[filterGroups][0][filters][0][condition_type]=eq&searchCriteria[currentPage]=" + str(temp) + "&searchCriteria[pageSize]=200&fields=items[sku]"

    res = requests.get(API_URL, headers=headers)
    # print res.text
    print(res.json().get('items'))
    print(len(res.json().get('items')))
    print(res.status_code)
    print(res.reason)
    print(temp)
    if len(res.json().get('items')) < 200:
        break
    temp += 1

