from django.conf.urls import patterns, url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_category', views.add_category, name='add_category'),
    url(r'^add_page', views.add_page, name='add_page'),
    url(r'^category/(?P<category_id>\d)/$', views.category, name='category'),
]
