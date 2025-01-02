from django import forms
from  travello.models import Guide, Booking

class BookingForm(forms.ModelForm):
    class Meta:
        accept_terms = forms.BooleanField(required=True)
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'email',
            'preferred_date',
            'party_size',
            'message',
            'accept_terms',
            'accept_marketing_emails'
   
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email address'}),
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'party_size': forms.NumberInput(attrs={'class': 'party-size'}),
            'message': forms.Textarea(attrs={'placeholder': 'Type your message here'}),
        }

class GuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = [
            'civility', 
            'first_name', 
            'last_name', 
            'email', 
            'phone_number',
            'country', 
            'city_or_region', 
            'mother_tongue', 
            'tour_languages',
            'presentation', 
            'photo', 
            'certified_guide', 
            'guide_card', 
            'message',
            'price'  # Include the new price field
        ]
        widgets = {
            'tour_languages': forms.TextInput(attrs={'placeholder': 'Enter at least one language'}),
            'presentation': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write a few lines about yourself'}),
            'message': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional message'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter your price per tour (in dollars)', 'step': '0.01'})  # Add widget for price
        }
