"""
import json
import requests
data = {
		  "option": {
			"label": "Not",
			"value": "Not_sure",
			"sort_order": 0,
			"is_default": True,
		  }
		}
	
API_URL = 'http://p236400.mittwaldserver.info/magento216/rest/V1/products/attributes/select_249/options'
TOKEN = 'g85930oxw74lqrwu51v9pff3ofa7y2af'
headers = {'Accept':'*/*','Content-Type':'applicaton/json','Authorization':'Bearer %s'%TOKEN}
res = requests.post(API_URL, data = json.dumps(data) ,headers = headers,verify=False)
print res.text
print res.status_code
print res.reason
"""
"""
import json
import requests
data = {
	  "option": {
		"label": "six",
		"value": "six",
		"sort_order": 0,
		"is_default": True,
		"store_labels": [
		  {
			"store_id": 4,
			"label": "Six"
		  }
		]
	  }
	}
	
API_URL = 'http://192.168.0.151/magento213/rest/V1/products/attributes/select_24/options'
TOKEN = 'c59xj3499s4johcuxujav8hrm1tos30x'
headers = {'Accept':'*/*','Content-Type':'applicaton/json','Authorization':'Bearer %s'%TOKEN}
res = requests.post(API_URL, data = json.dumps(data) ,headers = headers,verify=False)
#res = requests.get(API_URL,headers = headers,verify=False)
print res.text
print res.status_code
print res.reason

"""
import json
import timeit
import datetime
from php import Php
import urllib

import oauth2 as oauth
CONSUMER_KEY = '2yhthtqp3efy32uqbxxa595msvry5ex3'
TOKEN = 'c59xj3499s4johcuxujav8hrm1tos30x'
SECRET = 'dgbctrl1kr6ujigi2cjys520qwmdx89e'
CONSUMER_SECRET = 'x2o87hrrqon8h5xab4k1srk380decd2y'
#CONSUMER_KEY = '5yr3e0idkokkq8f71hsy7a5mx6kb8qk9'
#CONSUMER_SECRET = 'i9h05gkcypwiqee8dntlut69wnn764bj'
#TOKEN = 'kgt87uy6bmh3yj2c9ignf3np3ban9703'
#SECRET = '312ufoadx8g80pfh366smxt1ohvaaw75'
# your domain headers                                     customerCustomerRepositoryV1
#API_URL = 'http://192.168.1.118/mage2/index.php/rest/V1/customers/search'
#API_URL = 'http://p236400.mittwaldserver.info/magento2/rest/V1/products'
CONSUMER_KEY = 'ubxke62m1avmtaqgtc7npsqi8vm4h6na'
CONSUMER_SECRET = '0kgfaxi1pbhyc42jii2wtty4hcdw06fa'
TOKEN = 'g85930oxw74lqrwu51v9pff3ofa7y2af'
SECRET = '4t4qgildxk5t0d6p93dqrm4qbhwgw4mr'
#API_URL = 'http://192.168.0.151/magento213/rest/V1/products/attributes/select_24/options'
API_URL = 'http://p236400.mittwaldserver.info/magento216/rest/V1/products/attributes/select_249/options'
data = {
	  "option": {
		"label": "six",
		"value": "six",
		"sort_order": 0,
		"is_default": True,
		"store_labels": [
		  {
			"store_id": 4,
			"label": "Six"
		  }
		]
	  }
	}
	
client = None


def setup():
    global client
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth.Token(key=TOKEN, secret=SECRET)

    client = oauth.Client(consumer, token)
    pass

def test_update():
    global client
    #filters = {'searchCriteria':{'filterGroups':[{'filters':[{'field':'entity_id','value':"-1",'condition_type':'gt'}]}]}}
    #qs = Php.http_build_query(filters)
    #url = API_URL + qs
    #url = API_URL + '/'+ urllib.quote('24-MB04')
    #print type(url)
    
    
    headers = {'Accept': '*/*', 'Content-Type': 'application/json','Authorization':'Bearer g85930oxw74lqrwu51v9pff3ofa7y2af'}
    resp, content = client.request(
        API_URL,
        method='POST', body=json.dumps(data),headers=headers)
    print API_URL
    print resp
    print content
    


setup()
test_update()
