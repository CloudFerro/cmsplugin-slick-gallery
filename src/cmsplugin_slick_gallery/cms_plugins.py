from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import SlickGalleryPlugin
from django.utils.translation import ugettext as _


class SlickGalleryPluginBase(CMSPluginBase):
    name = _('Slick gallery')
    model = SlickGalleryPlugin
    render_template = "cmsplugin_slick_gallery/_slick_gallery_plugin.html"
    allow_children = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


plugin_pool.register_plugin(SlickGalleryPluginBase)
