from django.contrib import admin
from .models import Botinfos,Typeofsocialnetwork,Botinfosindiffrentsocnet,Countries,Contentgroupofbot,Dataofbots,Contentwebsiteofbot
from .models import Thesis,Oungroupofbot,Dataofoungroupofbots,Spreadata,Spreadatainfomonitoring,Articlesonothersitemonitoring,Articlesonothersitemonitoringdata
from .models import Monitoringbotonline,Monitoringbotonlinedata,Historypublishtobotandgroupsfromsiteandgroups,SearchopengroupinvK,Analysisofaccount,Cities,Listofcontentgroupofbot,Settingsanswers


class SettingsanswersAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Settingsanswers._meta.fields]
admin.site.register(Settingsanswers,SettingsanswersAdmin)

class ListofcontentgroupofbotAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Listofcontentgroupofbot._meta.fields]
admin.site.register(Listofcontentgroupofbot,ListofcontentgroupofbotAdmin)

class CountriesAdmin(admin.ModelAdmin):
  list_display = ('id', 'name_country')
admin.site.register(Countries,CountriesAdmin)

class BotinfosAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Botinfos._meta.fields]
admin.site.register(Botinfos,BotinfosAdmin)

class ContentgroupofbotAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Contentgroupofbot._meta.fields]
admin.site.register(Contentgroupofbot,ContentgroupofbotAdmin)

class DataofbotsAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Dataofbots._meta.fields]
admin.site.register(Dataofbots,DataofbotsAdmin)

class ContentwebsiteofbotAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Contentwebsiteofbot._meta.fields]
admin.site.register(Contentwebsiteofbot,ContentwebsiteofbotAdmin)

class ThesisAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Thesis._meta.fields]
admin.site.register(Thesis,ThesisAdmin)

class OungroupofbotAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Oungroupofbot._meta.fields]
admin.site.register(Oungroupofbot,OungroupofbotAdmin)

class SpreadataAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Spreadata._meta.fields]
admin.site.register(Spreadata,SpreadataAdmin)

class DataofoungroupofbotsAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Dataofoungroupofbots._meta.get_fields()]
admin.site.register(Dataofoungroupofbots)

class SpreadatainfomonitoringAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Spreadatainfomonitoring._meta.get_fields()]
admin.site.register(Spreadatainfomonitoring)

class ArticlesonothersitemonitoringAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Articlesonothersitemonitoring._meta.get_fields()]
admin.site.register(Articlesonothersitemonitoring,ArticlesonothersitemonitoringAdmin)

class ArticlesonothersitemonitoringdataAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Articlesonothersitemonitoringdata._meta.get_fields()]
admin.site.register(Articlesonothersitemonitoringdata,ArticlesonothersitemonitoringdataAdmin)

class TypeofsocialnetworkAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Typeofsocialnetwork._meta.fields]
admin.site.register(Typeofsocialnetwork,TypeofsocialnetworkAdmin)

class BotinfosindiffrentsocnetAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Botinfosindiffrentsocnet._meta.fields]
admin.site.register(Botinfosindiffrentsocnet,BotinfosindiffrentsocnetAdmin)

class MonitoringbotonlineAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Monitoringbotonline._meta.get_fields()]
admin.site.register(Monitoringbotonline,MonitoringbotonlineAdmin)

class MonitoringbotonlinedataAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Monitoringbotonlinedata._meta.get_fields()]
admin.site.register(Monitoringbotonlinedata,MonitoringbotonlinedataAdmin)

class HistorypublishtobotandgroupsfromsiteandgroupsAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Historypublishtobotandgroupsfromsiteandgroups._meta.get_fields()]
admin.site.register(Historypublishtobotandgroupsfromsiteandgroups,HistorypublishtobotandgroupsfromsiteandgroupsAdmin)

class SearchopengroupinvKAdmin(admin.ModelAdmin):
  list_display = [f.name for f in SearchopengroupinvK._meta.get_fields()]
admin.site.register(SearchopengroupinvK,SearchopengroupinvKAdmin)

class AnalysisofaccountAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Analysisofaccount._meta.get_fields()]
admin.site.register(Analysisofaccount,AnalysisofaccountAdmin)

class CitiesAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Cities._meta.fields]
admin.site.register(Cities,CitiesAdmin)











