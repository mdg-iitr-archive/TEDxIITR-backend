from __future__ import unicode_literals

from django.db import models


class Event(models.Model):
    theme = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    timestamp = models.DateField()
    image = models.ImageField(upload_to='events', blank=True, null=True)
    venue = models.CharField(max_length=200)
    index = models.IntegerField(default=0)

    def __str__(self):
        return self.theme


class Speaker(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    date = models.DateField()
    about = models.TextField()
    facebook = models.URLField(null=True)
    linkedin = models.URLField(null=True)
    twitter = models.URLField(null=True)
    profile_pic = models.ImageField(upload_to='speakers', null=True, blank=True)
    event = models.ForeignKey(Event, related_name='speaker')

    def __str__(self):
        return self.name


class Organizer(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    facebook = models.URLField(null=True)
    linkedin = models.URLField(null=True)
    twitter = models.URLField(null=True)
    profile_pic = models.ImageField(upload_to='speakers')

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    image = models.ImageField(upload_to='sponsors', null=True, blank=True)
    event = models.ForeignKey(Event, related_name='sponsor')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    duration = models.IntegerField(default=30)
    SCHEDULE_TYPES = (
        ('df', 'Default'),
        ('br', 'Break'),
    )
    type = models.CharField(max_length=7, choices=SCHEDULE_TYPES)
    speaker = models.ForeignKey(Speaker, related_name='talk', blank=True, null=True)

    def __str__(self):
        return self.title
