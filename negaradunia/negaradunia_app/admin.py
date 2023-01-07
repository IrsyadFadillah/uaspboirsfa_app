from django.contrib import admin

# Register your models here.
from .models import *

class bukuadmin(admin.ModelAdmin):
    list_display = ['nama_negara', 'letak_astronomi', 'ibu_kota', 'mata_uang', 'bahasa_resmi','bentuk_pemerintahan',]
    search_fields = ['nama_negara', 'letak_astronomi', 'ibu_kota', 'mata_uang', 'bahasa_resmi','bentuk_pemerintahan',]
    list_filter = ['benua_id']
    list_per_page = 4

admin.site.register(Negara, bukuadmin)
admin.site.register(Benua)
admin.site.register(Konservasi)
