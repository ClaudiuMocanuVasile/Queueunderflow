from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Community)
admin.site.register(Question)
admin.site.register(QueueUser)
admin.site.register(Answer)
admin.site.register(Comment)