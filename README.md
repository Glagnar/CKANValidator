#CKANValidator
This extension will make all changes to datasets private. After a validation phase the dataset
can be made active again by a user with the correct access rights

**IMPORTANT Settings:**
**The username below will be granted access to publish datasets**
	ckan.setstateforpendingvalidation.user = ***
	ckan.auth.create_unowned_dataset = false
	ckan.auth.create_dataset_if_not_in_organization = false

How 

	import urllib2
	import urllib
	import json
	import pprint


	# We'll use the package_show function to fetch the dataset
	fetchrequest = urllib2.Request('http://localhost:5000/api/action/package_show?id=8fe39f59-c218-432c-8796-c2938f228073')

	# Fetching private data and updating it requires an authorization header.
	# Replace *** with your API key, from your user account on the CKAN site
	fetchrequest.add_header('Authorization', 'a1b8e735-f3f1-44ac-ac24-5204f1ae3e43')

	# Make the HTTP request.
	fetchresponse = urllib2.urlopen(fetchrequest)

	assert retchresponse.code == 200

	# Use the json module to load CKAN's response into a dictionary.
	fetchresponse_dict = json.loads(fetchresponse.read())
	assert fetchresponse_dict['success'] is True

	# package_create returns the created package as its result. Print this for debugging
	# datasetpackage = fetchresponse_dict['result']
	# pprint.pprint(datasetpackage)

	# Set private to false
	fetchresponse_dict['result']['private'] = False

	data_string = urllib.quote(json.dumps(fetchresponse_dict['result']))

	# Now make a new request to update the dataset
	updaterequest = urllib2.Request('http://localhost:5000/api/action/package_update')

	# Updating a dataset requires an authorization header.
	# Replace *** with your API key, from your user account on the CKAN site
	# that you're creating the dataset on.
	updaterequest.add_header('Authorization', 'a1b8e735-f3f1-44ac-ac24-5204f1ae3e43')

	# Make the HTTP request.
	updateresponse = urllib2.urlopen(updaterequest, data_string)

	assert updateresponse.code == 200

	# Use the json module to load CKAN's response into a dictionary.
	updateresponse_dict = json.loads(updateresponse.read())
	assert response_dict['success'] is True

	# package_create returns the created package as its result.
	updated_package = updateresponse_dict['result']
	pprint.pprint(updated_package)

