from django.test import TestCase
from django.contrib.auth.models import User

from datetime import date
from decimal import Decimal

from mentha.models import Account, Transaction, Payee


class TransactionTestCase(TestCase):
	def setUp(self):
		self.test_user = User.objects.create_user('Fakey Fakerson', 'fake@test.com', 'notreal')
		self.test_account = Account.objects.create(name='Test Account', owner=self.test_user, balance=Decimal('1000.50'))

	def test_debit_transaction_from_csv(self):
		pre_balance = self.test_account.balance
		t = Transaction.objects.create_from_csv(self.test_account, '03/03/2014,-15.40,14062002,7411 Amazon Web Services aws.amazon.c WA 14062002')
		self.assertEqual(t.date, date(2014, 03, 03))
		self.assertEqual(t.amount, Decimal('15.40'))
		self.assertEqual(t.payee, Payee.objects.get(fi_name='7411 Amazon Web Services aws.amazon.c WA 14062002'))
		self.assertEqual(self.test_account.balance, pre_balance - Decimal('15.40'))

	def test_credit_transaction_from_csv(self):
		pre_balance = self.test_account.balance
		t = Transaction.objects.create_from_csv(self.test_account, '03/07/2014,428.37,,STARBUCKS CORP IL 01719891')
		self.assertEqual(t.date, date(2014, 03, 07))
		self.assertEqual(t.amount, Decimal('428.37'))
		self.assertEqual(t.payee, Payee.objects.get(fi_name='STARBUCKS CORP IL 01719891'))
		self.assertEqual(self.test_account.balance, pre_balance + Decimal('428.37'))

	def test_transaction_from_csv_with_preexisting_payee(self):
		payee = Payee.objects.create(name='Starbucks', fi_name='STARBUCKS CORP IL 01719891', owner=self.test_user)
		t = Transaction.objects.create_from_csv(self.test_account, '03/07/2014,428.37,,STARBUCKS CORP IL 01719891')
		self.assertEqual(t.payee.name, payee.name)
