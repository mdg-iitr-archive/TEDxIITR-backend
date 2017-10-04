# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'index.html')


def about(request):
  return render(request, 'about.html')

def talks(request):
  return render(request, 'talks.html')

def sponsors(request):
  return render(request, 'sponsors.html')

def events(request):
  return render(request, 'events.html')
