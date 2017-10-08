from rest_framework import serializers

from talks.models import *


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'index', 'theme', 'description', 'timestamp', 'image', 'venue')


class SpeakerSerializer(serializers.ModelSerializer):
    event_index = serializers.IntegerField(source='event.index')

    class Meta:
        model = Speaker
        fields = (
            'name', 'designation', 'date', 'about', 'facebook', 'linkedin', 'twitter', 'profile_pic', 'event_index')


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = ('name', 'designation', 'facebook', 'linkedin', 'profile_pic', 'twitter')


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'link', 'image')


class ScheduleSerializer(serializers.ModelSerializer):
    speaker = SpeakerSerializer()
    
    class Meta:
        model = Schedule
        fields = ('title', 'description', 'start_time', 'duration', 'type', 'speaker')
