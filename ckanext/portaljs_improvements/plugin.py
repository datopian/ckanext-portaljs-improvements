import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.portaljs_improvements import actions

class PortaljsImprovementsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IActions)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'portaljs_improvements')

    # IActions
    def get_actions(self):

        return {
            'package_create': actions.package_create,
            'package_update': actions.package_update,
            'group_create': actions.group_create,
            'group_update': actions.group_update,
            'organization_create': actions.organization_create,
            'organization_update': actions.organization_update
        }