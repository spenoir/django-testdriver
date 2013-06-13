import os

from . import settings

from django.views.generic import TemplateView

from django_testdriver.utils import ParseTestDriverYaml

class JasmineSpecRunnerView(TemplateView):
    """
    This view renders stdout from management command
    and parses the conf
    """
    template_name = "django_testdriver/base.html"

    def get_context_data(self, **kwargs):
        context = super(JasmineSpecRunnerView, self).get_context_data(**kwargs)

        conf = ParseTestDriverYaml(os.path.join(settings.SITE_ROOT,
                            settings.JSTESTDRIVER_CONFIG)).conf

        context.update({
            'jstestdriver_conf': conf
        })
        return context

custom_spec_runner = JasmineSpecRunnerView.as_view()


class JasmineCoverageView(TemplateView):
    template_name = "html/index.html"

coverage_view = JasmineCoverageView.as_view()