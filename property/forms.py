from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image,Listing,Timeslot,Booking


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30,  required=False, help_text='Optional.')
    username= forms.CharField(max_length=30,required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
  

    class Meta:
        model = User
        fields = ('username', 'name', 'email',
                  'password1', 'password2')

# class NewProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         exclude = ['user','bio'] 
#         widgets = {
#             'tags': forms.CheckboxSelectMultiple(),
#         }



class NewImageForm(forms.ModelForm):
	class Meta:
		model = Image
        # exclude = ['user',]
		fields = ['title', 'image_path']



class TimeForm(forms.ModelForm):
    # submit = SubmitField('Add Time') 
        model = Timeslot
        fields = ['date','start_time','end_time']       
        
        



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['user', 'profile']

class ListingForm(forms.ModelForm):

    # apartments = "aparts"
    # Bungalows = "bunga"
    # Massionettes = "mansion"

    # PROPERTY_CHOICES = [
    # (apartments, "apartments"),
    # (Bungalows, "bungalows"),
    # (Massionettes, "Massionattes")
    # ]


    # title = forms.CharField(max_length=50,  required=False)
    # location = forms.CharField(max_length=30,required=False)
    # category = forms.CharField( widget=forms.Select(choices=PROPERTY_CHOICES,),required=True)
    # description = forms.CharField(max_length=50,  required=False)
    # bedrooms = forms.CharField(max_length=30,required=False)
    # pricing = forms.DecimalField(max_digits=6, decimal_places=2)
    # featured_pic_path = forms.ImageField()
    
  



    class Meta:
        model = Listing
        # exclude=['user']
        fields=['title','location','category','description','bedrooms','pricing','featured_pic_path']    


class TimeslotForm(forms.ModelForm):
    class Meta:
        model = Timeslot 
        exclude=['user']
        fields=[]  
