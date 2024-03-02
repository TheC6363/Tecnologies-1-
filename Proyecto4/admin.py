from django.contrib import admin

from Proyecto4.models import Language,Framework

admin.site.register([Language, Framework])
# admin.site.register(Framework)