from django.conf.urls import url
from djangoTestApp01 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]