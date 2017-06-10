from django import forms
from .models import Spreadata
from .models import SearchopengroupinvK
from .models import Analysisofaccount



class Spreadataform(forms.ModelForm):
      class Meta:
            model = Spreadata     
            fields = ('spread_date','spread_link','spread_img','spread_text','thesis','botwhopost')
			

class SearchopengroupinvKform(forms.ModelForm):	
        class Meta:
            model = SearchopengroupinvK     
            fields = ('name_of_group','min_count_of_people')		
			
class Analysisofaccountform(forms.ModelForm):	
        class Meta:
            model = Analysisofaccount     
            fields = ('name_of_account',)	
			
