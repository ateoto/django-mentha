from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from .views import HomeView, UploadTransactionView, TransactionView

urlpatterns = patterns('',
	url(r'^/$', HomeView.as_view(), name='mentha-home'),
	url(r'^upload/$', login_required(UploadTransactionView.as_view()), name='mentha-upload'),
	url(r'^transactions/$', login_required(TransactionView.as_view()), name='mentha-transactions'),
	url(r'^transactions/(?P<category>[-\w]+)/$', login_required(TransactionView.as_view()), name='mentha-transactions'),
)