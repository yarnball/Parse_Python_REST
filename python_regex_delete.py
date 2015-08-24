while True:
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

	# Gets all the object IDs we need to delete in this request
	batchRequests = []
	for obj in result["results"]:
		request = { "method": "DELETE", "path": "/1/classes/YourClass/%s" % obj["objectId"] }
		batchRequests.append(request)

	if len(batchRequests) == 0:
		print "Had no more requests, finishing..."
		break

	# Make the batch request to delete all the objects we recieved
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('POST', '/1/batch', json.dumps({
	       "requests": batchRequests[0:49]
	     }), {
       "X-Parse-Application-Id": "apikey",
       "X-Parse-REST-API-Key": "apikey",
	    "Content-Type": "application/json"
	     })
	result = json.loads(connection.getresponse().read())
	print result

print "Done"