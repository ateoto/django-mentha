import logging
from django.views.generic.base import TemplateView


logger = logging.getLogger('dev.console')

class HomeView(TemplateView):
    template_name = "mentha/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        logger.info('This is all here for an example.')

        return context
