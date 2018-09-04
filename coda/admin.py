from django.contrib import admin
from coda.models import Paziente, Priority

#admin.site.register(Paziente)

class PazienteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'rif' ,'t_arrival', 'priority_code', 'priority_val')

# Register your models here.

admin.site.register(Priority)
admin.site.register(Paziente, PazienteAdmin)
