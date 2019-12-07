import json
import timeit
import datetime
from php import Php
import urllib

import oauth2 as oauth

CONSUMER_KEY = 'ubxke62m1avmtaqgtc7npsqi8vm4h6na'
CONSUMER_SECRET = '0kgfaxi1pbhyc42jii2wtty4hcdw06fa'
TOKEN = 'g85930oxw74lqrwu51v9pff3ofa7y2af'
SECRET = '4t4qgildxk5t0d6p93dqrm4qbhwgw4mr'
API_URL = 'http://p236400.mittwaldserver.info/magento216/rest/V1/products/attributes'

data = {
	  "attribute": {
		"is_wysiwyg_enabled": True,
		"is_html_allowed_on_front": True,
		"used_for_sort_by": True,
		"is_filterable": True,
		"is_filterable_in_search": True,
		"is_used_in_grid": True,
		"is_visible_in_grid": True,
		"is_filterable_in_grid": True,
		"position": 0,
		"is_visible": True,
		"scope": "global",
		"attribute_code": "select_9",
		"frontend_input": "select_9",
		"entity_type_id": "text",
		"is_required": False,
		"is_user_defined": False,
		"default_frontend_label": "select_9",
		"type" : "char",
		"frontend_labels": [
		  {
			"store_id": 7,
			"label": "None"
		  }
		],
		
		"custom_attributes": [
		  {
			"attribute_code": "select_9",
			"value": "91"
		  }
		]
	  }
	}

def setup():
    global client
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth.Token(key=TOKEN, secret=SECRET)

    client = oauth.Client(consumer, token)
    pass

def test_update():
    global client
    headers = {'Accept': '*/*', 'Content-Type': 'application/json','Authorization':'Bearer g85930oxw74lqrwu51v9pff3ofa7y2af'}
    resp, content = client.request(API_URL, method='POST', body=json.dumps(data),headers=headers)
    print API_URL
    print resp
    print content


setup()
test_update()
