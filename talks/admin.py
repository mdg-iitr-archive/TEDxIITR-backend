from django.contrib import admin
from talks.models import *

admin.site.register(Event)
admin.site.register(Speaker)
admin.site.register(Organizer)
admin.site.register(Sponsor)
