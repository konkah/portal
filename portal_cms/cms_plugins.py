from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from .models import Poseidon
from .debug import log

@plugin_pool.register_plugin
class PoseidonPlugin(CMSPluginBase):
    model = Poseidon
    name = "Poseidon"
    render_template = "poseidon/highlights/columns.html"
    cache = False

    def render(self, context, instance, placeholder):
        if instance.type == "columns":
            setattr(instance, 'columns', [{'highlights': instance.highlights}])
        else:
            self.render_template = self.render_template.replace("columns", instance.type)

        context = super().render(context, instance, placeholder)

        return context
