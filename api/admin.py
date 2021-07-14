from django.contrib import admin
from api.models import Friend, Belonging, Borrowed


admin.site.register(Friend)
admin.site.register(Belonging)
admin.site.register(Borrowed)