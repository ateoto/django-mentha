from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Account, Transaction


class UploadTransactionForm(forms.Form):
    account = forms.ModelChoiceField(queryset=Account.objects.all())
    transaction_file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(UploadTransactionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(Submit('submit', 'Submit'))

    def process_transactions(self):
        account = self.cleaned_data['account']

        for csv_line in self.cleaned_data['transaction_file']:
            Transaction.objects.create_from_csv(account, csv_line)