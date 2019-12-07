import requests
TOKEN = 'g85930oxw74lqrwu51v9pff3ofa7y2af'
API_URL = 'http://p236400.mittwaldserver.info/magento216/rest/V1/products/attributes/'
sku = 'url_key'
#sku = 'product_1?store_id=0'
API_URL += sku
headers = {'Accept':'*/*','Content-Type':'application/json','Authorization':'Bearer %s'%TOKEN}
print API_URL
res = requests.get(API_URL,headers = headers,verify=False)
print res.text
print res.status_code
print res.reason
