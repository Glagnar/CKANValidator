#CKANValidator
Force validation of resources

IMPORTANT:

Set: ckan.auth.create_unowned_dataset = false

**The username below will be granted access to publish datasets**
*Set: ckan.setstateforpendingvalidation.user = glagnar*

How 

import urllib2
import urllib
import json
import pprint

**Put the id of the dataset here**
	dataset_dict = {
        	'id': '5e4ed304-3183-4c09-a606-41f09eadaf5f',
        	'private': False,
	}

**Use the json module to dump the dictionary to a string for posting.**
	data_string = urllib.quote(json.dumps(dataset_dict))

	#Use the URL of the instance here
	request = urllib2.Request('http://localhost:5000/api/action/package_update')

	# Updating a dataset requires an authorization header.
	# Replace *** with your API key, from your user account specified for the user at ckan.setstateforpendingvalidation.user
	# that you're creating the dataset on.
	request.add_header('Authorization', '***')
	
	# Make the HTTP request.
	response = urllib2.urlopen(request, data_string)
	
	assert response.code == 200
	
	# Use the json module to load CKAN's response into a dictionary.
	response_dict = json.loads(response.read())
	assert response_dict['success'] is True
	
	# package_create returns the created package as its result.
	created_package = response_dict['result']
	pprint.pprint(created_package)
