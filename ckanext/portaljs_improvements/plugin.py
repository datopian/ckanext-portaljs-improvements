import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.portaljs_improvements import actions


class PortaljsImprovementsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IConfigurable)
    plugins.implements(plugins.IActions)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
                             'portaljs_improvements')

    def configure(self, config):
        # Certain config options must exists for the plugin to work. Raise an
        # exception if they're missing.
        missing_config = "{0} is not configured. Please amend your .ini file."
        config_options = (
            'ckanext.portaljs_improvements.portal_url',
            'ckanext.portaljs_improvements.portal_secret',
        )
        for option in config_options:
            if not config.get(option, None):
                raise RuntimeError(missing_config.format(option))

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
