from django.contrib import admin

# Register your models here.
from app.models import *
# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecords)
