from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Company)
admin.site.register(Project)
admin.site.register(Person)
admin.site.register(Story)
admin.site.register(Ticket)