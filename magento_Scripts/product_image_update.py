import requests
import json
API_URL = 'http://p236400.mittwaldserver.info/magento216/rest/johnnyurban_english/V1/products/'
TOKEN = 'g85930oxw74lqrwu51v9pff3ofa7y2af'
#API_URL = 'http://192.168.0.151/magento213/rest/all/V1/products/'
#TOKEN = '0vkwajywx49ckjdhuv6uvxi961riusrx'

data = {
	'entry': 
			{'disabled': False, 
			'media_type':'image',
			'position': 0, 
			'types': ['thumbnail'], 
			'id' : 389
			}
} 

sku = '10032M'
API_URL += sku +'/media/389'
headers = {'Accept':'*/*','Content-Type':'application/json','Authorization':'Bearer %s'%TOKEN}
res = requests.put(API_URL,headers = headers,data=json.dumps(data),verify=False)
print res.text
print res.status_code
print res.reason



