from django.contrib import admin
from .models import Bedaia,Nukhba
# Register your models here.


class BedaiaModelAdmin(admin.ModelAdmin):
    list_display=('title','created_at','update_at')
    search_fields=('title','discription')
    list_per_page = 1


class NukhbaModelAdmin(admin.ModelAdmin):
    list_display=('title','created_at','update_at')
    search_fields=('title','discription')
    list_per_page = 1
admin.site.register(Bedaia, BedaiaModelAdmin)
admin.site.register(Nukhba , NukhbaModelAdmin)