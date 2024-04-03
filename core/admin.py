from django.contrib import admin
from .models import Movie,Profile,Video,CustomUser
# Register your models here.

admin.site.register([Movie,Profile,Video,CustomUser])
