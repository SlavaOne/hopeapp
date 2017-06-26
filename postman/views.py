# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .models import Tableofresources,Tableofounemails,Sendingletters,Yesno
from django.core.mail import send_mail
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time

######################################################################################################################################################################

def SendMessages(From,Password,To,Subject,Text,name_file_in_email,path_to_file):
    name_server=str(From).split("@")[1].split(".")[0]
    msg = MIMEMultipart()
    msg['From'] = From
    msg['To'] = To
    msg['Subject'] = Subject
    msg.attach(MIMEText(Text, 'plain'))

    if path_to_file!='Abracadabra':
       attachment = open(path_to_file, "rb")

       part = MIMEBase('application', 'octet-stream')
       part.set_payload((attachment).read())
       encoders.encode_base64(part)
       part.add_header('Content-Disposition', "attachment; filename= %s" % name_file_in_email)
       msg.attach(part)


    server = smtplib.SMTP('smtp.'+str(name_server)+'.com', 587)
    server.starttls()
    server.login(From, Password)
    text = msg.as_string()
    server.sendmail(From, To, text)
    server.quit()




def MainSendMess(From_Dict,Array_To,Subject_Mess,Main_Text,Attachment_Dict_Name_In_Email_and_Path_to_file,Is_Rain_Posting):
     Success=""
     if Is_Rain_Posting==0:# отправляем каждому отдельное сообщение
       for OneRiciever in Array_To:
           for OneKey in From_Dict.keys():
               SendMessages(OneKey, From_Dict[OneKey], OneRiciever, Subject_Mess, Main_Text, list(Attachment_Dict_Name_In_Email_and_Path_to_file.keys())[0], Attachment_Dict_Name_In_Email_and_Path_to_file[list(Attachment_Dict_Name_In_Email_and_Path_to_file.keys())[0]])


######################################################################################################################################################################

def nice_letter(request):# страница и форма распространения тнформации

    return_page_array={}
    return_page_array['transmitters']=Tableofounemails.objects.all()
    return_page_array['recievers']=Tableofresources.objects.all().order_by('id')
    return_page_array['answers']=Yesno.objects.all()
    
    if request.method == 'POST': 
        from_message = str(request.POST['id_transmitters'])
        to_message = json.loads(str(request.POST.getlist('id_reciever')).replace("'",'"'))
        subject_message=str(request.POST['subject_message'])
        text_message=str(request.POST['text_message'])
                
        NameEmailsOfRecievers=[]
        if from_message!="enter_reciever":
           if text_message!="" and subject_message!="":
            for EachChekedId in to_message:
        	    NameEmail=Tableofresources.objects.values_list('e_mail').filter(id=EachChekedId)[0][0]
        	    NameEmailsOfRecievers.append(NameEmail)
            From_email=Tableofounemails.objects.values_list('e_mail').filter(id=from_message)[0][0]
            From_password=Tableofounemails.objects.values_list('password').filter(id=from_message)[0][0]
            for OneEmail in NameEmailsOfRecievers:
                                                  SendMessages(From_email,From_password,OneEmail,subject_message,text_message,'Abracadabra','Abracadabra')
            text_success="Рассылка выполнена успешно!"
            return HttpResponseRedirect(request, 'postman/nice_letter.html',{'page_array':return_page_array,'success':text_success})
        else:
        	text_success="Введите тему и текст сообщения!"
        	return render(request, 'postman/nice_letter.html')
    else:
         text_success="Заполните данные форм!"
         return render(request, 'postman/nice_letter.html',{'page_array':return_page_array,'success':text_success})









