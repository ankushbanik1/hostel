from django.contrib import admin

# Register your models here.
from . models import complain

# admin.site.register(complain)

 
class complainAdmin(admin.ModelAdmin):
    list_display = ('name', 'Email', 'message')
 
admin.site.register(complain, complainAdmin)