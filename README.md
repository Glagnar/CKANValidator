#CKANValidator
This extension will make all changes to datasets private. After a validation phase the dataset
can be made active again by a user with the correct access rights

###IMPORTANT Settings:
###The username below will be granted access to publish datasets
	ckan.setstateforpendingvalidation.user = ***
	ckan.auth.create_unowned_dataset = false
	ckan.auth.create_dataset_if_not_in_organization = false
