import json
import requests
data = {'product':
	{
	  "sku" : "00110011",
	  "name": "Binary",
	  "attribute_set_id": 1,
	  "price": 0,
	  "status": 1,
	  "visibility": 4,
	  "type_id": "simple",
	 
	  "weight": 10,
	  
	'custom_attributes':
	 [{'attribute_code': u'preorder_availability', 'value': False}, 
	 {'attribute_code': u'quantity_and_stock_status', 'value': u'1'}, 
	 {'attribute_code': u'options_container', 'value': u'container2'}, 
	 {'attribute_code': u'cost', 'value': 5.0}, 
	 {'attribute_code': u'media_gallery', 'value': ''}, 
	 {'attribute_code': u'wk_preorder', 'value': 0}, 
	 {'attribute_code': u'url_key', 'value': ''}, 
	 {'attribute_code': u'demo123', 'value': ''},
	  {'attribute_code': u'msrp_display_actual_price_type', 'value': u'1'}, 
	  {'attribute_code': u'page_layout', 'value': u'1column'},
	   {'attribute_code': u'tax_class_id', 'value': u'2'},
	    {'attribute_code': u'category_ids', 'value': [2]}, 
	    {'attribute_code': u'meta_keyword', 'value': ''}, 
	    {'attribute_code': u'short_description', 'value': ''}, {'attribute_code': u'custom_layout', 'value': u'empty'}, 
	    {'attribute_code': u'meta_description', 'value': ''}, {'attribute_code': u'meta_title', 'value': ''}, 
	    {'attribute_code': u'description', 'value': u'Chocopie 123'}, {'attribute_code': u'news_to_date', 'value': False},
	     {'attribute_code': u'news_from_date', 'value': False}, {'attribute_code': u'is_product_saleable', 'value': 1}, 
	     {'attribute_code': u'tier_price', 'value': ''}, {'attribute_code': u'special_price', 'value': 10.0}, 
	     {'attribute_code': u'gallery', 'value': ''}, {'attribute_code': u'is_rentable', 'value': 0}, 
	     {'attribute_code': u'custom_design', 'value': u'2'},
	      {'attribute_code': u'special_to_date', 'value': '2017-05-30'},
	        {'attribute_code': u'msrp', 'value': 0.0}]
	        
    }
}

	
API_URL = 'http://192.168.0.151/magento213/rest/V1/products'
TOKEN = '0vkwajywx49ckjdhuv6uvxi961riusrx'
headers = {'Accept':'*/*','Content-Type':'applicaton/json','Authorization':'Bearer %s'%TOKEN}
res = requests.post(API_URL, data = json.dumps(data) ,headers = headers,verify=False)
print res.text
print res.status_code
print res.reason
