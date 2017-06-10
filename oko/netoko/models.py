from django.db import models
from django.utils import timezone


class Countries(models.Model):# страны 
      name_country = models.CharField(max_length=50)
      def __str__(self):
        return self.name_country
      class Meta:
        verbose_name_plural = 'Страны'
	  
class Cities(models.Model):# города
      name_of_city = models.CharField(max_length=50,default='')
      coordinates = models.CharField(max_length=50,default='')
      def __str__(self):
        return self.name_of_city
      class Meta:
        verbose_name_plural = 'Города'
	 
class Typeofsocialnetwork(models.Model):
      name_of_socnet = models.CharField(max_length=50,default='')
      url_to_group_link = models.CharField(max_length=70,default='')
      name_to_accaunt_page = models.CharField(max_length=70,default='')
      def __str__(self):
        return self.name_of_socnet
      class Meta:
        verbose_name_plural = 'Тип социальной сети'
		
class Botinfos(models.Model):   # боты
      country_of_bot_id = models.ForeignKey(Countries,default='')
      city_of_bot = models.ForeignKey(Cities,default='')
      name_of_bot = models.CharField(max_length=200)
      surname = models.CharField(max_length=200)
      describe = models.TextField() 
      created_date = models.DateTimeField(default=timezone.now)
      def __str__(self):
        return self.name_of_bot
      class Meta:
        verbose_name_plural = 'Боты'
		
class Settingsanswers(models.Model):
      answer = models.CharField(max_length=10,default='')
      def __str__(self):
        return self.answer
      class Meta:
        verbose_name_plural = 'Ответы'
	  
class Botinfosindiffrentsocnet(models.Model):# данные на ботов (пароли, токены, логины ) в разных социальных сетях
      bot_id = models.ForeignKey(Botinfos)
      type_of_social_net = models.ForeignKey(Typeofsocialnetwork)
      email_phone = models.CharField(max_length=200,default='')
      password = models.CharField(max_length=200,default='')
      id_in_ss = models.CharField(max_length=30,default='')
      describe = models.TextField()
      access_token = models.CharField(max_length=200,default='')
      auto_pilot = models.ForeignKey(Settingsanswers, null=True)
      def __str__(self):
        return self.email_phone	
      class Meta:
        verbose_name_plural = 'Данные на ботов в различных сетях'
	  
class Dataofbots(models.Model):   # данные по всем ботам
      bot_id = models.ForeignKey(Botinfos)
      count_of_friends = models.CharField(max_length=10)   
      type_of_social_net = models.CharField(max_length=20,default='')
      date_mark = models.DateTimeField(default=timezone.now)	
      class Meta:
        verbose_name_plural = 'Статистические данные на аккаунты ботов'	  

class Oungroupofbot(models.Model): # группы которые ведут боты
      bot_id = models.ForeignKey(Botinfos,default='')
      name_cont_group = models.CharField(max_length=200,default='')
      id_group_in_ss = models.CharField(max_length=20,default='')
      describe = models.CharField(max_length=200,default='')
      type_of_social_net = models.ForeignKey(Typeofsocialnetwork,default='')
      def __str__(self):
        return self.name_cont_group	  
      class Meta:
        verbose_name_plural = 'Группы, которые ведут боты'
		
class Listofcontentgroupofbot(models.Model):
      name_cont_group = models.CharField(max_length=200,default='')
      id_group_in_ss = models.CharField(max_length=20,default='')
      type_of_social_net = models.ForeignKey(Typeofsocialnetwork,default='')
      describe = models.CharField(max_length=200,default='')
      def __str__(self):
        return self.name_cont_group	  
      class Meta:
        verbose_name_plural = 'Список групп для наполнения контента'
	  
class Contentgroupofbot(models.Model): # группы, из которых берется инфа для ботов
      bot_id = models.ForeignKey(Botinfosindiffrentsocnet,default='')
      group_id = models.ForeignKey(Listofcontentgroupofbot,default='')
      class Meta:
        verbose_name_plural = 'Настройка ведения позиций'
      
	  
class Contentwebsiteofbot(models.Model): # сайты, из которых берутся ссылки для наполнения
      bot_id = models.ForeignKey(Botinfos)
      name_cont_site = models.CharField(max_length=200,default='')
      adres_page_to_content_link = models.CharField(max_length=20,default='')
      describe = models.CharField(max_length=200,default='')
      def __str__(self):
        return self.name_cont_site	
      class Meta:
        verbose_name_plural = 'Сайты из которых набирается информация'
class Thesis(models.Model):# # тезисы для работы 
      bot_id = models.ForeignKey(Botinfos,default='')
      country_of_thesis = models.ForeignKey(Countries)
      describe_thesis = models.CharField(max_length=200,default='')
      created_date = models.DateTimeField(default=timezone.now)
      def __str__(self):
        return self.describe_thesis	
      class Meta:
        verbose_name_plural = 'Тезисы для работы'
	  
class Dataofoungroupofbots(models.Model):   # данные по всем группам, которые ведут боты
      bot_id = models.ForeignKey(Oungroupofbot)
      count_of_friends = models.CharField(max_length=10,default='') 
      group_id = models.CharField(max_length=30,default='') 
      date_mark = models.DateTimeField(default=timezone.now)
      class Meta:
        verbose_name_plural = 'Статистические данные групп, которые ведут боты'
	  
class Spreadata(models.Model): # материал для распространения
      spread_date = models.DateTimeField(default=timezone.now)
      spread_link = models.CharField(max_length=200,default='')
      spread_img = models.CharField(max_length=200,default='')
      typess = models.ForeignKey(Typeofsocialnetwork,default='')
      spread_text = models.CharField(max_length=2500,default='')
      groups_to_spread = models.CharField(max_length=1000,default='')
      thesis = models.ForeignKey(Thesis,default='')
      botwhopost = models.ForeignKey(Botinfos,default='')
      class Meta:
        verbose_name_plural = 'Распространение информации'
	  
class Spreadatainfomonitoring(models.Model): # мониторинг распространенного материала
      bot_id = models.ForeignKey(Botinfos,default='')
      type_of_social_net = models.ForeignKey(Typeofsocialnetwork,default='')	
      id_spread_entity = models.ForeignKey(Spreadata)
      spreadinf_comment = models.CharField(max_length=3,default='')# text of comments
      spreadinf_likes = models.CharField(max_length=3,default='')# only count
      spreadinf_date = models.DateTimeField(default=timezone.now)
      class Meta:
        verbose_name_plural = 'Статистические данные распространенной информации'
	  
class Articlesonothersitemonitoring(models.Model): # адреса статей на сайтах
      httpadres_of_article = models.ForeignKey(Spreadata)
      name_of_article = models.CharField(max_length=200,default='')
      bot_id = models.ForeignKey(Botinfos)
      def __str__(self):
        return self.name_of_article	
      class Meta:
        verbose_name_plural = 'Статьи с сайтов для мониторинга'
	  
	  
class Articlesonothersitemonitoringdata(models.Model): # данные по количеству просмотров статьи на сайте
      time_of_monitoring = models.DateTimeField(default=timezone.now)
      count_of_views = models.CharField(max_length=200,default='')
      article_id = models.ForeignKey(Articlesonothersitemonitoring)
      def __str__(self):
        return self.article_id	
      class Meta:
        verbose_name_plural = 'Данные статей с сайтов для мониторинга'
	  
	  
class Monitoringbotonline(models.Model): # мониторинг онлайн или нет 
      name = models.CharField(max_length=50,default='')
      describe = models.CharField(max_length=200,default='')
      id_bot = models.CharField(max_length=200,default='')
      def __str__(self):
        return self.name
      class Meta:
        verbose_name_plural = 'Мониторинг онлайна'		
	 
class Monitoringbotonlinedata(models.Model): # данные по онлайн мониторингу
      time = models.DateTimeField(default=timezone.now)
      status = models.CharField(max_length=200,default='')
      class Meta:
        verbose_name_plural = 'Данные мониторинга онлайн'		
	  
class Historypublishtobotandgroupsfromsiteandgroups(models.Model): # история ссылок публикаций по всем ботам и группам со всех ботов и групп
     name_of_link = models.CharField(max_length=200,default='')
     name_of_bot_or_group = models.CharField(max_length=200,default='')
     class Meta:
        verbose_name_plural = 'Таблица истории публикаций'		
	 
class SearchopengroupinvK(models.Model):# класс поиск открытых групп вк (для формы)
      name_of_group = models.CharField(max_length=50,default='')
      min_count_of_people = models.CharField(max_length=10,default='')
      def __str__(self):
        return self.name_of_group	
      class Meta:
        verbose_name_plural = 'Поиск открытых групп Вконтакте'		
	  
class Analysisofaccount(models.Model):# класс анализа аккаунта (для формы)
      name_of_account = models.CharField(max_length=100,default='')
      def __str__(self):
        return self.name_of_account	
      class Meta:
        verbose_name_plural = 'Анализ аккаунта Вконтакте'		
      