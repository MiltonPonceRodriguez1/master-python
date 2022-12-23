from django.contrib import admin
from .models import Page

# Configuración extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content') # Buscador
    list_filter = ('visible', ) # Filtrar por campos del modelo
    list_display = ('title', 'visible', 'created_at') # Mostrar solo algunas colums del modelo
    ordering = ('-created_at',) # Criterio de ordenación

# Register your models here.
admin.site.register(Page, PageAdmin)

# Configuración del panel
title = "Proyecto con Django"
subtitle = "Panel de Gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
