from django.contrib import admin
from .models import catagori
# Register your models here.
class catagoryadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
admin.site.register(catagori,catagoryadmin)