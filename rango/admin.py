from django.contrib import admin
from rango.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Question)
admin.site.register(Choice)