from rest_framework import serializers

from talks.models import *


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'theme', 'description', 'timestamp', 'image')


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = ('name', 'designation', 'date', 'about', 'facebook', 'linkedin', 'twitter', 'profile_pic')


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = ('name', 'designation', 'facebook', 'linkedin', 'profile_pic', 'twitter')


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'link', 'image')
