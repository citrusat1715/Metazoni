from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from accounts.models import UserAddress
from django.forms.extras import widgets

User = get_user_model()


class SignUpForm(UserCreationForm):


    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'email', 'password1', 'password2','is_active','avatar','dob' )

class UserAddressForm(forms.ModelForm):
   def __init__(self, *args, **kwargs):
        super(UserAddressForm, self).__init__(*args, **kwargs)
        # Making name required
        self.fields['phone1'].required = True
        self.fields['shippingAddress1'].required = True
        self.fields['shippingState'].required = True
        self.fields['shippingCity'].required = True
        self.fields['firstName'].required=True
        self.fields['lastName'].required=True


   
   class Meta:
       model=UserAddress
       exclude=('user',)     
        
class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # Making name required
        self.fields['email'].widget.attrs['readonly'] = True
    dob = forms.DateField(widget=widgets.SelectDateWidget())
    class Meta:
        model=User
        fields = ('email', 'first_name', 'last_name','is_active','avatar','dob' )
        
       
       

