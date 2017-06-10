from django.shortcuts import render
from django.utils import timezone
from .models import Countries,Botinfos,Contentgroupofbot
from selenium import webdriver
from .forms import Spreadataform
from .forms import SearchopengroupinvKform
from .forms import Analysisofaccountform
from django.shortcuts import redirect
from .spreadcode import *
import sqlite3
from .fusioncharts import FusionCharts


############################################

def CreateGraphic(Data,Id,width,height):
    datamydata='<script type="text/javascript"> FusionCharts.ready(function () { new FusionCharts({"type": "column2d", "id": "ex'+str(Id)+'", "width": "'+str(width)+'", "height": "'+str(height)+'", "renderAt": "dynamic_div_'+str(Id)+'", "dataFormat": "json", "dataSource": {"chart": {"caption": "", "subCaption": "", "numberPrefix": "", "theme": "ocean"}, "data": '+str(Data)+'}}); }); </script> <script type="text/javascript"> FusionCharts.ready(function () { FusionCharts("ex'+str(Id)+'").render(); }); </script>'
    return datamydata

############################################



def start_page(request):# стартовая страница

    conn = sqlite3.connect('R:\\Django\\DjangoBotNetControl\\oko\\db.sqlite3')
    c = conn.cursor()
	
    dict_to_return={}#massive to return with data of main table and data with table of bot's and group's
	
    dict_of_main_tables={}# данные для главной таблицы у карты
    
    c.execute("SELECT count(*) FROM netoko_countries")
    dict_of_main_tables['country']=(c.fetchall()[0][0])

    c.execute("SELECT count(*) FROM netoko_oungroupofbot")
    dict_of_main_tables['botgroups'] = (c.fetchall()[0][0])

    c.execute("SELECT count(*) FROM netoko_botinfos")
    dict_of_main_tables['bots'] = (c.fetchall()[0][0])

    c.execute("SELECT count(*) FROM netoko_oungroupofbot")
    dict_of_main_tables['auditory'] = 1234
	
    dict_to_return['main_table']=dict_of_main_tables
		
    dict_of_table_group=c.execute("SELECT * FROM netoko_oungroupofbot").fetchall()# данные для таблицы групп
	
    dict_of_table_bot=c.execute("SELECT * FROM netoko_botinfos").fetchall()# данные для таблицы ботов,сначала смотрим уникальных ботов, потом проходимся по соц сетям и выводим в каких они зареганы и списко друзей
	
	
    dict_to_return['bots']=[]
    for onebotcortej in dict_of_table_bot:
        botinfo={}		
        botinfo['id']=onebotcortej[0]
        botinfo['name']=onebotcortej[1]
        botinfo['surname']=onebotcortej[2]
        botinfo['describe']=onebotcortej[3]
        botinfo['date_create']=onebotcortej[5]
		
		# Все аккаунты бота в социальных сетях
        botinfo['all_accounts']=[]
		
        all_accounts_of_bot_select=c.execute("SELECT id_in_ss,type_of_social_net_id FROM netoko_botinfosindiffrentsocnet WHERE bot_id_id ='"+str(onebotcortej[0])+"'").fetchall()
        for i in all_accounts_of_bot_select:
                 name_socnet=c.execute("SELECT name_of_socnet,name_to_accaunt_page FROM netoko_typeofsocialnetwork WHERE id ='"+str(i[1])+"'").fetchall()
                 bot_cortej={}
                 bot_cortej['id_bot_in_socnet']=i[0]
                 bot_cortej['type_ss']=name_socnet[0][0]
                 bot_cortej['url_to_page']=name_socnet[0][1]
                 botinfo['all_accounts'].append(bot_cortej)
        
		#город бота
        city_select=c.execute("SELECT name_of_city FROM netoko_cities WHERE id ='"+str(onebotcortej[4])+"'").fetchall()
        
        botinfo['city']=city_select[0][0]
		
		#страна бота
        country_select=c.execute("SELECT name_country FROM netoko_countries WHERE id ='"+str(onebotcortej[6])+"' order by name_country").fetchall()
        botinfo['country']=country_select[0][0]
		
        botinfo['groups_of_bot']=[]
		
		#группы, которые ведут боты
        group_of_bots_select=c.execute("SELECT name_cont_group,id_group_in_ss,type_of_social_net_id FROM netoko_oungroupofbot WHERE bot_id_id ='"+str(onebotcortej[0])+"'").fetchall()
        for eachcortejgroup in group_of_bots_select:
            dict_of_group={}
            dict_of_group['name_of_group']=eachcortejgroup[0]
            dict_of_group['id_group_in_ss']=eachcortejgroup[1]
            dict_of_group['type_of_social_net_id']=eachcortejgroup[2]
            botinfo['groups_of_bot'].append(dict_of_group)
   	
        botinfo['country']=country_select[0][0]
		
        data=[{"label": "January", "value": "880000"}, {"label": "February", "value": "730000"}, {"label": "Mart", "value": "590000"}, {"label": "April", "value": "520000"}]
        column2d = CreateGraphic(data,onebotcortej[0],450,200)
        botinfo['dynamic_graphic']=column2d
		
		
		
       
        dict_to_return['bots'].append(botinfo)
		
    dict_to_return['groups']=[]		
    for onegroupcortej in dict_of_table_group:	
        groupinfo={}
        groupinfo['id']=onegroupcortej[0]
        groupinfo['name']=onegroupcortej[1]		
        groupinfo['id_in_ss']=onegroupcortej[2]
        groupinfo['describe']=onegroupcortej[3]
		
        bot_select=c.execute("SELECT name_of_bot,surname FROM netoko_botinfos WHERE id ='"+str(onegroupcortej[4])+"'").fetchall()
        groupinfo['bot']=str(bot_select[0][0])+" "+str(bot_select[0][1])
        
        type_ss_select=c.execute("SELECT name_of_socnet FROM netoko_typeofsocialnetwork WHERE id ='"+str(onegroupcortej[5])+"'").fetchall()
        groupinfo['type_of_socialnet']=str(type_ss_select[0][0])
		
		
        dict_to_return['groups'].append(groupinfo)
	
   	
    c.close()
    conn.close()
    return render(request, 'netoko/start_page.html', {'page_dict':dict_to_return})

def kml_country_page(request):# ссылка на файл "граница стран"
    return render(request, 'netoko/kml_country_page.kml', {})
	
def geo_object(request):# ссылка на файл с объектами на карте
    return render(request, 'netoko/geo_object.kml', {})
		
def spread_page(request):# страница и форма распространения тнформации
    if request.method == "POST":
       form = Spreadataform(request.POST)
       if form.is_valid():
          spread_date = request.POST['spread_date']
          spread_link = request.POST['spread_link']
          spread_img = request.POST['spread_img']
          spread_text = request.POST['spread_text']
          thesis = request.POST['thesis']
          botwhopost = request.POST['botwhopost']
          #if first_name=='324':
            #  driver = webdriver.Chrome('C:\\Users\\Hp\\Anaconda3\\Lib\\chromedriver.exe')
          return redirect('netoko/start_page.html')
    else:
         form = Spreadataform()
    return render(request, 'netoko/spread_page.html', {'form': form})
	
def editor_page(request):# страница редактирования информации в системе(пока не работает. Данные вносятся в админке)
    return render(request, 'netoko/editor_page.html')
	
def search_group_page(request):# страница с поиском групп вк
    if request.method == "POST":
       form = SearchopengroupinvKform(request.POST)
       if form.is_valid():
          search_group_word = request.POST['name_of_group']
          return redirect('netoko/search_group_page.html')
    else:
         form = SearchopengroupinvKform()
    return render(request, 'netoko/search_group_page.html', {'form': form})
	
	
def analysis_page(request):# анализ аккаунта
    if request.method == "POST":
       form = Analysisofaccountform(request.POST)
       if form.is_valid():
          search_group_word = request.POST['name_of_group']
          return redirect('netoko/analysis_page.html')
    else:
         form = Analysisofaccountform()
    return render(request, 'netoko/analysis_page.html', {'form': form})
	
def demo_page(request):# демо страница для тренировок
	 
    d=[{"label":"Piter", "value":"880000"},{"label":"John", "value":"730000"},{"label":"Sofia", "value":"590000"},{"label":"Fedor", "value":"520000"}]
    x=CreateGraphic(d)
         # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return  render(request, 'netoko/demo_page.html',{'dictionary':{'output' : x}})
	
def onlinemonitoring(request):# демо страница для тренировок
	 
    return  render(request, 'netoko/onlinemonitoring.html')
    
def drive_page(request):# демо страница для тренировок
	 
    return  render(request, 'netoko/drive_page.html')
  
		  
