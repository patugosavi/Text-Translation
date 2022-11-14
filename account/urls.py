from django.urls import include, path
from account.views import *

app_name = 'account'

urlpatterns = [

path('texttranslation',texttranslation,name='texttranslation'),

]