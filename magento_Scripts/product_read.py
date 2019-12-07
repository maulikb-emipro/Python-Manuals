"""
data = {
  "product": {
    "sku": "000111",
    "name": "Dairymilk",
    "attribute_set_id": 21,
    "price": 20,
    "status": 1,
    "visibility": 1,
    "type_id": "simple",
    "weight": 10,
    "saveOptions": True
}
}

data = {'product': 
	    {
		  'sku': u'0011001112',
		  u'status': u'1', 
		  'name': u'Loreal123', 
		  'weight': 0.0, 
		  'type_id': u'simple', 
		  'price': 200.0, 
		  'attribute_set_id': u'4', 
		  'created_at': u'2017-05-20 06:06:55', 
		  'visibility': 4, 
	      'saveOptions' : True,
	}
}

data = {'product': {'sku': '0011-215-HE', 'status': '1', 'name': 'RedMi 3s', 'weight': 200.0, 'type_id': 'simple', 'price': 9000.0, 'attribute_set_id': '4', 'custom_attributes': [{'attribute_code': 'quantity_and_stock_status', 'value': '1'}, {'attribute_code': 'options_container', 'value': 'container2'}, {'attribute_code': 'cost', 'value': 6000.0}, {'attribute_code': 'media_gallery', 'value': ''}, {'attribute_code': 'url_key', 'value': ''}, {'attribute_code': 'demo123', 'value': ''}, {'attribute_code': 'tax_class_id', 'value': '2'}, {'attribute_code': 'meta_keyword', 'value': ''}, {'attribute_code': 'custom_layout_update', 'value': ''}, {'attribute_code': 'short_description', 'value': ''}, {'attribute_code': 'meta_description', 'value': ''}, {'attribute_code': 'meta_title', 'value': ''}, {'attribute_code': 'description', 'value': ''}, {'attribute_code': 'news_to_date', 'value': False}, {'attribute_code': 'news_from_date', 'value': False}, {'attribute_code': 'tier_price', 'value': ''}, {'attribute_code': 'gallery', 'value': ''}, {'attribute_code': 'special_from_date', 'value': False}, {'attribute_code': 'special_to_date', 'value': False}, {'attribute_code': 'custom_design_from', 'value': False}, {'attribute_code': 'custom_design_to', 'value': False}, {'attribute_code': 'msrp', 'value': 0.0}], 'visibility': '4'}},
		

		



import json
import requests
API_URL = 'http://192.168.0.151/magento213/rest/V1/products'
TOKEN = 'c59xj3499s4johcuxujav8hrm1tos30x'
headers = {'Accept':'*/*','Content-Type':'applicaton/json','Authorization':'Bearer %s'%TOKEN}
#res = requests.post(API_URL,headers = headers,verify=False)
#res = requests.post(API_URL, data.get(body), headers = headers,verify=False)
res = requests.post(API_URL,data=json.dumps(data),headers=headers)
print res.text
print res.status_code
print res.reason
"""	


import urllib2

sku = "947-:987-489"
#sku1 = urllib2.quote(sku)
print sku1






