#product_write_script
import requests
import urllib2
sku = 'GM_BLACK'
#sku1 = urllib2.quote(sku)
API_URL = 'http://192.168.0.149/Ankita/magentoS2/rest/V1/products/%s'%sku
TOKEN = 'duwavxgusj64kyjne65mo9g6p4sbu1gk'
headers = {'Accept':'*/*','Content-Type':'application/json','Authorization':'Bearer %s'%TOKEN}
res = requests.get(API_URL,headers=headers,verify=False)
print res.text
print res.status_code
print res.ok
