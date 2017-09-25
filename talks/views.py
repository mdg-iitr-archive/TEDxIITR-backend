from django.shortcuts import render
from rest_framework import generics
from talks.serializers import *


class EventView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class SpeakerView(generics.ListCreateAPIView):
    serializer_class = SpeakerSerializer
    queryset = Speaker.objects.all()


class SpeakerYearView(generics.ListAPIView):
    serializer_class = SpeakerSerializer

    def get_queryset(self):
        return Speaker.objects.filter(date__year=self.kwargs['year'])


class OrganizerView(generics.ListCreateAPIView):
    serializer_class = OrganizerSerializer
    queryset = Organizer.objects.all()


class SponsorView(generics.ListCreateAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()
