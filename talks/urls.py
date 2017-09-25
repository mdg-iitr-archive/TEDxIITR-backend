from django.conf.urls import url

from talks import views

urlpatterns = [
    url('events/$', views.EventView.as_view(), name='events'),
    url('speakers/$', views.SpeakerView.as_view(), name='speakers'),
    url('speakers/(?P<year>[0-9]+)/$', views.SpeakerYearView.as_view(), name='speakers-year'),
    url('organizers/$', views.OrganizerView.as_view(), name='organizers'),
    url('sponsors/$', views.SponsorView.as_view(), name='sponsors'),
]
