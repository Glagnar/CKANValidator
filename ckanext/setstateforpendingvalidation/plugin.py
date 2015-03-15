import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

log = logging.getLogger(__name__)

class SetStateForPendingValidationPlugin(plugins.SingletonPlugin):
   plugins.implements(plugins.IPackageController, inherit=True)

   def after_create(self, context, data_dict):
    log.info("CKAN after_create self: %r", self)
    log.info("CKAN after_create context: %r", context)
    log.info("CKAN after_create data_dict: %r", data_dict)
    
    aboutToUpdate = {
            'private': True,
    }

    if 'id' not in data_dict:
        pass

    aboutToUpdate['id'] = data_dict['id']
    if 'state' not in data_dict or ( 'state' in data_dict and data_dict['state'] == 'active'):
        if 'private' not in data_dict or ( 'private' in data_dict and data_dict['private'] == False):
            log.info("CKAN to send %r: ", aboutToUpdate)
            toolkit.get_action('package_update')(context, aboutToUpdate)


   def after_update(self, context, data_dict):
    log.info("CKAN after_update self: %r", self)
    log.info("CKAN after_update context: %r", context)
    log.info("CKAN after_update data_dict: %r", data_dict)
    
    aboutToUpdate = {
            'private': True,
    }

    if 'id' not in data_dict:
        pass

    aboutToUpdate['id'] = data_dict['id']
    if 'state' not in data_dict or ( 'state' in data_dict and data_dict['state'] == 'active'):
        if 'private' not in data_dict or ( 'private' in data_dict and data_dict['private'] == False):
            log.info("CKAN to send %r: ", aboutToUpdate)
            toolkit.get_action('package_update')(context, aboutToUpdate)

