from django.conf.urls import url
from . import views



urlpatterns = [
url(r'^netoko', views.start_page, name='start_page'),
url(r'^spread', views.spread_page, name='spread_page'),
url(r'^editor', views.editor_page, name='editor_page'),
url(r'^search', views.search_group_page, name='search_group_page'),
url(r'^kml', views.kml_country_page, name='kml_country_page'),
url(r'^geo_object', views.geo_object, name='geo_object'),
url(r'^analysis', views.analysis_page, name='analysis_page'),
url(r'^demo', views.demo_page, name='demo_page'),
url(r'^onlinemonitoring', views.onlinemonitoring, name='onlinemonitoring'),
url(r'^drive_page', views.drive_page, name='drive_page'),
]