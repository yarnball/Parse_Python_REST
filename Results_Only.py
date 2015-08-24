	# Finds genpants that start with "wherethisappears"
	import json,httplib,urllib
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	params = urllib.urlencode({"where":json.dumps({
	       "link": {
	         "$regex": "^wherethisappears"
	       }
	     })})
	connection.connect()
	connection.request('GET', '/1/classes/YourClass?%s' % params, '', {
       "X-Parse-Application-Id": "apikey",
       "X-Parse-REST-API-Key": "apikey"
	     })
	result = json.loads(connection.getresponse().read())
	print result