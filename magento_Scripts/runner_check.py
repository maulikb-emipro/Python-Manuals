vals = {
	'user': 'magento10', 
	'host': 'localhost', 
	'password': 'magento10', 
	'port': 5432, 
	'database': 'magento10'
	}
dsn_str = ''
vals.pop('database')
print vals
for k,v in vals.iteritems():
	dsn_str += "%s=%s "%(k,v)

print dsn_str
