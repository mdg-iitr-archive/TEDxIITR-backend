from rest_framework import generics
from talks.serializers import *


class EventView(generics.ListAPIView):
    """
        Returns the list of all the events
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class SpeakerView(generics.ListAPIView):
    """
        Returns the list of all the speakers
    """
    serializer_class = SpeakerSerializer
    queryset = Speaker.objects.all()


class SpeakerYearView(generics.ListAPIView):
    """
        Returns the list of speakers year-wise
    """
    serializer_class = SpeakerSerializer

    def get_queryset(self):
        return Speaker.objects.filter(date__year=self.kwargs['year'])


class SpeakerEventView(generics.ListAPIView):
    """
        Returns the list of speakers event-wise
    """
    serializer_class = SpeakerSerializer

    def get_queryset(self):
        return Speaker.objects.filter(event__index=self.kwargs['event'])


class OrganizerView(generics.ListAPIView):
    """
        returns the list of organizers
    """
    serializer_class = OrganizerSerializer
    queryset = Organizer.objects.all()


class SponsorView(generics.ListAPIView):
    """
        returns the list of sponsors
    """
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()


class SponsorsEventView(generics.ListAPIView):
    """
        returns the list of sponsors event-wise
    """
    serializer_class = SponsorSerializer

    def get_queryset(self):
        return Speaker.objects.filter(event__index=self.kwargs['event'])
