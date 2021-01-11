from django.contrib import admin
from home.models import Contact
from home.models import Info
from home.models import News

# Register your models here.
admin.site.register(Contact)
admin.site.register(Info)
admin.site.register(News)