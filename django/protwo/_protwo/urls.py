from django.conf.urls import url
from _protwo import views

app_name = '_protwo'

urlpatterns = [
    url('user/',views.user,name='user'),
    url('form/',views.form,name='form')
]
