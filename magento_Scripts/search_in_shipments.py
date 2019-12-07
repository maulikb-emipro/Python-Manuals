


import json
import timeit
import datetime
from php import Php
import urllib

import oauth2 as oauth

# oauth constants - enter yours here
#CONSUMER_KEY = 'p0a20bw6ena9rqwvn4likvvowmmwhc66'
#CONSUMER_SECRET = 'v0q0ipqgfftefj0ssabdd6qxqn86w1y6'
#TOKEN = '02vfb8k3da4hriip2d58toyely6s0166'
#SECRET = 'chs2hplod2qt9ku1gx16pxg4oh9py08j'


CONSUMER_KEY = '72u7jsbd7ye61p4odypdocrlnywxnd9q'
CONSUMER_SECRET = 'hl7u9dpn341a4n2ihrgfxdo78a156pi1'
TOKEN = 'aoym4qdwafgid2640hqmnwmjl2nsj5fc'
SECRET = 't8207apnp721hrj50i5u7jc0mad7msdb'


#API_URL = 'http://m2zc5.test.dev.zococity.es/rest/V1/shipments?'
API_URL = 'http://erptest.mage2.emiprotechnologies.com/rest/V1/products?'
client = None


def setup():
    global client
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth.Token(key=TOKEN, secret=SECRET)

    client = oauth.Client(consumer, token)
    pass

def test_update():
    global client
    
    #filters = {'searchCriteria':{'filterGroups':[{'filters':[{'field':'entity_id','value':"0",'condition_type':'gt'}]}]}}
    #filters = {'searchCriteria':{'filterGroups':[{'filters':[{'field':'order_id','value':"72",'condition_type':'eq'}]}]}}
    #filters = {'searchCriteria':{'filterGroups':[{'filters':[{'field':'order_id','value':"60",'condition_type':'eq'}]}]}}
    filters = {'searchCriteria':{'filterGroups':[{'filters':[{'field':'entity_id','value':'2045,2046','condition_type':'in'}]}]}}
    qs = Php.http_build_query(filters)
    url = API_URL+qs
    #url = API_URL
    print url
  
    headers = {'Accept': '*/*', 'Content-Type': 'application/json','Authorization':'Bearer aoym4qdwafgid2640hqmnwmjl2nsj5fc'}
    resp, content = client.request(
        url,
        method='GET', body=json.dumps({}),headers=headers)
    print resp
    print content
    #print json.dumps(f)
    


setup()
test_update()
#http://192.168.1.7/magento2/pub/media/catalog/product/m/b//mb01-blue-0.jpg
