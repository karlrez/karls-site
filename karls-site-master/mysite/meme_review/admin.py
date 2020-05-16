from django.contrib import admin
from .models import MemeUpload, Comment
# Register your models here.
admin.site.register(MemeUpload)
admin.site.register(Comment)
