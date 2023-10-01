from django.contrib import admin
from .models import *


"""class CategoryAdmin(Admin.ModelAdmin):
    list_display = ('name' , ' image' , 'description')
    admin.site.register(Catagory,CategoryAdmin)
    
"""
admin.site.register(Catagory)
admin.site.register(Product)



# Register your models here.

