import logging

from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import get_list_or_404
from django.core.urlresolvers import reverse_lazy

from .forms import UploadTransactionForm
from .models import Account, Transaction


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
    success_url = reverse_lazy('mentha-transactions', kwargs={'category': 'uncategorized'})

    def form_valid(self, form):
        logger.info(form.cleaned_data['account'])
        form.process_transactions()
        logger.info(form.cleaned_data['account'])
        return super(UploadTransactionView, self).form_valid(form)

class TransactionView(ListView):
    model = Transaction
    template_name = 'mentha/transactions.html'

    def get_queryset(self):
        try:
            if self.kwargs['category'] == 'uncategorized':
                return Transaction.objects.filter(category=None)
            else:
                return get_list_or_404(Transaction, category__slug=self.kwargs['category'])
                get_object_or_404logger.info(self.kwargs['category'])
        except KeyError:
            return Transaction.objects.all()