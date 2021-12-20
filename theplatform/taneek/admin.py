from django.contrib import admin
from .models import *

admin.site.register(Posts)

admin.site.register(Details)
admin.site.register( displayusername)
admin.site.register(ConnectedUser)