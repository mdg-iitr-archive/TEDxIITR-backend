# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from itertools import groupby

from talks.models import Event, Speaker, Organizer, Sponsor

# Create your views here.
def extract_date(entity):
    'extracts the starting date from an entity'
    return entity.date

def index(request):
  speakers = Speaker.objects.all()
  context = {
    'speakers' : speakers
  }
  return render(request, 'index.html', context)


def about(request):
  organizers = Organizer.objects.all()
  context = {
    'organizers' : organizers
  }
  return render(request, 'about.html', context)

def talks(request):
  speakers = Speaker.objects.order_by('date')
  list_of_speakers = { t:list(g) for t, g in groupby(speakers, key=extract_date)}

  context = {
    'list_of_speakers' : list_of_speakers
  }
  return render(request, 'talks.html', context)

def sponsors(request):
  sponsors = Sponsor.objects.all()
  context = {
    'sponsors' : sponsors
  }
  return render(request, 'sponsors.html',context)

def events(request):
  events = Event.objects.all()
  context = {
    'events' : events
  }
  return render(request, 'events.html',context)
