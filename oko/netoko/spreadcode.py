# -*- coding: UTF-8 -*-
import requests,json

token='f196c23fd14c26f4bb0ebfe6e91d920e9a61ef31ad56f39bfc504765561fd992cdbc9c8935d5547ff2325'

###########################################################################Функции поиска групп############################################################################
def Search(Token,SearchWord):
    ReturnMass=[]
    url = "https://api.vk.com/method/groups.search?q="+str(SearchWord)+'&access_token='+str(Token)+ '&count=1000'
    page = requests.get(url)
    html = page.text
    MyDict = json.loads(html)
    for OneGroupData in MyDict['response']:
        if type(OneGroupData)!=int:
            ReturnMass.append(OneGroupData['gid'])
    return ReturnMass

def CheckGroupToPost(ArrayGroupToCheck, MinCountOfUser):
    ReturnArray=[]
    Only=ArrayGroupToCheck[0:300]
    StringOfGroups=str(Only).replace(" ","").replace("[","").replace("]","")
    url = "https://api.vk.com/method/groups.getById?group_ids="+str(StringOfGroups)+"&fields=can_post,members_count,description"
    page = requests.get(url)
    html = page.text
    MyDict = json.loads(html)
    for OneGroup in MyDict["response"]:
        if "can_post" in OneGroup.keys():
           if OneGroup["is_closed"] == 0 and OneGroup["can_post"] == 1 and OneGroup["members_count"]>MinCountOfUser:
               ReturnArray.append(OneGroup)
    return ReturnArray

def MainDefSearch(SearchWord,token):
    Groups = Search(token, SearchWord)
    GroupsToPost = CheckGroupToPost(Groups, 1000)
    return GroupsToPost
####################################################################################################################################################################


###########################################################################Функции распространения############################################################################




	
	
	
	
	
	
	
	
	