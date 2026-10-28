from django import forms
from .models import MovieModel
from .models import UsersModel
from .models import Booking


class MovieModelForm(forms.ModelForm):
    class Meta():
        model=MovieModel
        fields=['mname','director','rating','genre','price','avail']
        
        
class UserModelForm(forms.ModelForm):
    class Meta():
        model=UsersModel
        fields=['name','contact','email','addr']
        
        
class BookingModelForm(forms.ModelForm):
    class Meta():
        model=Booking
        fields=['users','movies','mov_date','tickets']