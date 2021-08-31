from django.contrib import admin
from .models import *

admin.site.site_header = "KIB Admin"
admin.site.site_title = "KIB Admin Portal"
admin.site.index_title = "Welcome to KIB Portal"

admin.site.register(Blog)

# Register your models here.
