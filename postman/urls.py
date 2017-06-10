from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'nice_letter', views.nice_letter, name='nice_letter'),
]