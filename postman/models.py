from django.db import models
from django.utils import timezone



class Yesno(models.Model):   
      answer = models.CharField(max_length=10,default='', null=True)
      def __str__(self):
         label=   self.answer
         return label     
      class Meta:
        verbose_name_plural = 'Да/Нет'


class Whoarethey(models.Model):
      legend = models.CharField(max_length=200,default='', null=True) 
      class Meta:
        verbose_name_plural = 'Таблица должностей получателя'
      def __str__(self):
         label=   self.legend
         return label

class Tableofresources(models.Model):   
      organization_name = models.ForeignKey(Whoarethey, null=True,default='',blank=True)
      e_mail = models.CharField(max_length=50,default='', null=True) 
      describe = models.CharField(max_length=1000,default='', null=True,blank=True) 
      name = models.CharField(max_length=50,default='', null=True,blank=True) 
      surname = models.CharField(max_length=50,default='', null=True,blank=True)
      def __str__(self):
         label=	" "+str(self.name)+" "+str(self.surname)+" "+ str(self.e_mail)
         return label	  
      class Meta:
        verbose_name_plural = 'Таблица e-mail адресов редакторов сайтов и администраторов групп в соцсетях'

class Whoarewe(models.Model):
      legend = models.CharField(max_length=200,default='', null=True) 
      class Meta:
        verbose_name_plural = 'Таблица легенд отправителя'
      def __str__(self):
         label=   self.legend
         return label	

class Tableofounemails(models.Model):   
      organization_name = models.ForeignKey(Whoarewe, null=True,blank=True)
      e_mail = models.CharField(max_length=50,default='', null=True) 
      describe = models.CharField(max_length=1000,default='', null=True,blank=True) 
      name = models.CharField(max_length=50,default='', null=True,blank=True) 
      surname = models.CharField(max_length=50,default='', null=True,blank=True)   
      password = models.CharField(max_length=50,default='', null=True) 
      phone_number = models.CharField(max_length=50,default='', null=True)
      def __str__(self):
         label=   str(self.name)+" "+str(self.surname)+" "+ str(self.e_mail)
         return label     
      class Meta:
        verbose_name_plural = 'Таблица почтовых ящиков отправителя'	
		
class Sendingletters(models.Model):
      from_message=models.ForeignKey(Tableofounemails, null=True,default='')
      target = models.ForeignKey(Tableofresources, null=True,default='')
      text_message = models.CharField(max_length=5000,default='', null=True,blank=True) 
      subject_message = models.CharField(max_length=500,default='', null=True,blank=True) 
      date_message = models.DateTimeField(default=timezone.now)
      is_rain_letter= models.ForeignKey(Yesno,default='', null=True)
      success_message = models.CharField(max_length=5,default='', null=True)
      class Meta:
        verbose_name_plural = 'Таблица отправленных e-mail'
      def __str__(self):
         label=	self.target+" ("+str(self.date_message)+")"
         return label	 



		 
