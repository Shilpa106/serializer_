from django.contrib import admin

# Register your models here.
from .models import Blog,Event,Comment,GameRecord
admin.site.register(Blog)
admin.site.register(Event)
admin.site.register(Comment)
admin.site.register(GameRecord)

