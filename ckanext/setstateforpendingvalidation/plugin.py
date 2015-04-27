import logging
import pylons.config as config

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

log = logging.getLogger(__name__)

def resource_create(context, data_dict = None):
    log.debug("CKAN resource_created")
    return {'success': True, 'msg': 'Access needed to see resources'}

class SetStateForPendingValidationPlugin(plugins.SingletonPlugin):
   plugins.implements(plugins.IPackageController, inherit=True)
   plugins.implements(plugins.IAuthFunctions, inherit=True)

   def get_auth_functions(self):
        return {'resource_create': resource_create} 

   def after_update(self, context, data_dict):
    log.debug("CKAN after_update context: %r", context)
    log.debug("CKAN after_update data_dict: %r", data_dict)
    
    # Check if the user is the one who is allowed to publish datasets
    userAllowedToPublish = config.get('ckan.setstateforpendingvalidation.user')
    if userAllowedToPublish == context['user']:
        log.info("User is allowed to publish dataset")
        return

    # Only do this for active datasets, and not ones in draft or deleted state
    # it is also not needed if the dataset is already private
    if 'state' not in data_dict or ( 'state' in data_dict and data_dict['state'] == 'active'):
        if 'private' not in data_dict or ( 'private' in data_dict and data_dict['private'] == False):
            data_dict['private'] = True
            log.info("CKAN to send %r: ", data_dict)
            toolkit.get_action('package_update')(context, data_dict)
