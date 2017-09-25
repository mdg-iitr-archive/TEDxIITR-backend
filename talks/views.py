from rest_framework import generics
from talks.serializers import *


class EventView(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class SpeakerView(generics.ListAPIView):
    serializer_class = SpeakerSerializer
    queryset = Speaker.objects.all()


class SpeakerYearView(generics.ListAPIView):
    serializer_class = SpeakerSerializer

    def get_queryset(self):
        return Speaker.objects.filter(date__year=self.kwargs['year'])


class SpeakerEventView(generics.ListAPIView):
    serializer_class = SpeakerSerializer

    def get_queryset(self):
        return Speaker.objects.filter(event__id=self.kwargs['event'])


class OrganizerView(generics.ListAPIView):
    serializer_class = OrganizerSerializer
    queryset = Organizer.objects.all()


class SponsorView(generics.ListAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()


class SponsorsEventView(generics.ListAPIView):
    serializer_class = SponsorSerializer

    def get_queryset(self):
        return Speaker.objects.filter(event__id=self.kwargs['event'])
