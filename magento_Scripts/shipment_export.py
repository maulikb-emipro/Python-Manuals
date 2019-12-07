import json
import requests

data = {
	'items': [{
		'order_item_id': u'113', 
		'qty': 3.0
		}], 
	'tracks': [{
		'extension_attribute' : {},
		'carrier_code': u'flatrate', 
		'track_number': u'12345645456', 
		'title': u'Flat Rate'
		}], 
	'notify': True,
	}


API_URL = 'http://192.168.0.151/magento213/rest/V1/order/73/ship'
TOKEN = '0vkwajywx49ckjdhuv6uvxi961riusrx'
headers = {'Accept':'*/*','Content-Type':'applicaton/json','Authorization':'Bearer %s'%TOKEN}
res = requests.post(API_URL,headers = headers,data=json.dumps(data),verify=False)
print res.text
print res.status_code
print res.reason
