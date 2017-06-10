from django.contrib import admin
from .models import Tableofresources,Sendingletters,Tableofounemails,Yesno,Whoarewe,Whoarethey
from django.utils.translation import ugettext_lazy as _
# Register your models here.


class TableofresourcesAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Tableofresources._meta.fields]
admin.site.register(Tableofresources,TableofresourcesAdmin)

class SendinglettersAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Sendingletters._meta.fields]
admin.site.register(Sendingletters,SendinglettersAdmin)

class TableofounemailsAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Tableofounemails._meta.fields]
admin.site.register(Tableofounemails,TableofounemailsAdmin)

class YesnoAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Yesno._meta.fields]
admin.site.register(Yesno,YesnoAdmin)

class WhoareweAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Whoarewe._meta.fields]
admin.site.register(Whoarewe,WhoareweAdmin)

class WhoaretheyAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Whoarethey._meta.fields]
admin.site.register(Whoarethey,WhoaretheyAdmin)
