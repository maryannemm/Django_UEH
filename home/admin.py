from django.contrib import admin
from .models import Volunteer,contact,donor, team, program, testimony, OngoingEvent, PastEvent, FutureEvent
from .models import Resource



# Register your models here.


admin.site.register(Resource)
admin.site.register(Volunteer)
admin.site.register(donor)
admin.site.register(contact)
admin.site.register(team)
admin.site.register(program)
admin.site.register(testimony)
admin.site.register(OngoingEvent)
admin.site.register(PastEvent)
admin.site.register(FutureEvent)


