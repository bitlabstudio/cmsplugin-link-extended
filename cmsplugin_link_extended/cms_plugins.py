"""Implementation of CMSPluginBase class for ``cmsplugin_link_extended``."""
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugins.link.cms_plugins import LinkPlugin

from .forms import CustomLinkForm
from .models import LinkExtension


class ExtendedLinkPlugin(LinkPlugin):
    name = _('Link Extended')
    form = CustomLinkForm
    render_template = 'cmsplugin_link_extended/link.html'

    def render(self, context, instance, placeholder):
        context = super(ExtendedLinkPlugin, self).render(
            context, instance, placeholder)
        extension = None
        try:
            extension = LinkExtension.objects.get(link=instance)
        except LinkExtension.DoesNotExist:
            pass
        if extension:
            context.update({
                'css_classes': extension.css_classes,
            })
        return context


plugin_pool.register_plugin(ExtendedLinkPlugin)
