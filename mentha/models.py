import logging

from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from datetime import date, datetime
from decimal import Decimal


logger = logging.getLogger('dev.console')

class Account(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)

    def __str__(self):
        return '{}: ${}'.format(self.name, self.balance.quantize(Decimal('0.00')))

    def load_transactions_from_file(self, transaction_file):
        for line in transaction_file:
            Transaction.objects.create_from_csv(self, line)

class Category(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)

    def __str__(self):
        return self.name

class Budget(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey(Category)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)

class Payee(models.Model):
    name = models.CharField(max_length=100)
    fi_name = models.CharField(max_length=100, editable=False, blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    category = models.ForeignKey(Category, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name and self.fi_name:
            self.name = self.fi_name

        super(Payee, self).save(*args, **kwargs)

class TransactionManager(models.Manager):
    def create_from_csv(self, account, csv_string):
        parts = csv_string.split(',')

        t_datetime = datetime.strptime(parts[0], '%m/%d/%Y')
        t_date = date(t_datetime.year, t_datetime.month, t_datetime.day)

        amount = Decimal(parts[1])

        if amount < 0:
            amount = amount * -1
            transaction_type = 0
        else:
            transaction_type = 1

        payee, created = Payee.objects.get_or_create(fi_name=parts[3], owner=account.owner)

        if not created:
            category = payee.category
        else:
            category = None

        transaction = self.create(
            account=account,
            date=t_date,
            amount=amount,
            transaction_type=transaction_type,
            payee=payee,
            category=category
        )

        return transaction

class Transaction(models.Model):
    TYPE_CHOICES = (
        (0, 'Debit'),
        (1, 'Credit')
    )

    account = models.ForeignKey(Account)
    date = models.DateField(blank=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    transaction_type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=0)
    payee = models.ForeignKey(Payee)
    category = models.ForeignKey(Category, blank=True, null=True)
    objects = TransactionManager()
    
    def __str__(self):
        return '{} - ${} {} by {}'.format(
            str(self.date),
            self.amount.quantize(Decimal('0.00')),
            self.get_transaction_type_display(),
            self.payee.name
        )
    
    def save(self, *args, **kwargs):
        if not self.date:
            self.date = date.today()

        if self.transaction_type == 0:
            self.account.balance -= self.amount
        else:
            self.account.balance += self.amount
        self.account.save()

        super(Transaction, self).save(*args, **kwargs)


@receiver(pre_delete, sender=Transaction)
def transaction_pre_delete(sender, **kwargs):
    transaction = kwargs['instance']

    if transaction.transaction_type == 0:
        transaction.account.balance += transaction.amount
    else:
        transaction.account.balance -= transaction.amount
    transaction.account.save()
