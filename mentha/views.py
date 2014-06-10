import logging

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import UploadTransactionForm
from .models import Account

logger = logging.getLogger('dev.console')

class HomeView(TemplateView):
    template_name = "mentha/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        logger.info('This is all here for an example.')

        return context

class UploadTransactionView(FormView):
    template_name = 'mentha/transaction_upload.html'
    form_class = UploadTransactionForm

    def form_valid(self, form):
        logger.info(form.cleaned_data['account'])
        form.process_transactions()
        logger.info(form.cleaned_data['account'])
        return super(UploadTransactionView, self).form_valid(form)