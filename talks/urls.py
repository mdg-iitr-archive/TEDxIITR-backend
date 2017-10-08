from django.conf.urls import url
from django.conf.urls.static import static
from talks import views
from tedxiitr import settings

urlpatterns = [
    url('^events/$', views.EventView.as_view(), name='events'),
    url('^events/(?P<index>[0-9]+)/$', views.EventIndexView.as_view(), name='events-index'),
    url('^schedule/$', views.ScheduleView.as_view(), name='schedule'),
    url('^speakers/$', views.SpeakerView.as_view(), name='speakers'),
    url('^speakers/year/(?P<year>[0-9]+)/$', views.SpeakerYearView.as_view(), name='speakers-year'),
    url('^speakers/event/(?P<event>[0-9]+)/$', views.SpeakerEventView.as_view(), name='speakers-event'),
    url('^organizers/$', views.OrganizerView.as_view(), name='organizers'),
    url('^sponsors/$', views.SponsorView.as_view(), name='sponsors'),
    url('^sponsors/event/(?P<event>[0-9]+)/$', views.SponsorsEventView.as_view(), name='sponsors-event'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
