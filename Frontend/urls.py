from django.conf.urls import url

from . import views

app_name = 'menu'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^talks/$', views.talks, name='talks'),
    url(r'^sponsors/$', views.sponsors, name='sponsors'),
    url(r'^events/$', views.events, name='events')
]
