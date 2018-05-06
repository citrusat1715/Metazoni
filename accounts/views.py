from django.shortcuts import render
from accounts.forms import SignUpForm, UserAddressForm,UserForm
from accounts.models import UserAddress
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.response import TemplateResponse
from django.shortcuts import resolve_url
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import get_object_or_404

# Create your views here.
def signup(request):

    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)        
        if signup_form.is_valid():
            
            user = signup_form.save()
            user.save()            
            raw_password = signup_form.cleaned_data.get('password1')
            email= signup_form.cleaned_data.get('email')

            user = authenticate(email=email, password=raw_password)            
            login(request, user)
            return redirect('addCategory')
    else:
        signup_form = SignUpForm()
        
    return render(request, 'signup.html', {'sform': signup_form})

@login_required
def userAddress(request):
    
    print(UserAddress.objects.all())
    if request.method == 'POST':
     upForm = UserAddressForm(request.POST)
     if upForm.is_valid():
       shippingAddress1=upForm.cleaned_data['shippingAddress1']
       shippingAddress2=upForm.cleaned_data['shippingAddress2']
       shippingCity=upForm.cleaned_data['shippingCity']
       shippingState=upForm.cleaned_data['shippingState']
       phone1=upForm.cleaned_data['phone1']
       phone2=upForm.cleaned_data['phone2']
       user=request.user
       u=UserAddress(shippingAddress1=shippingAddress1, shippingAddress2=shippingAddress2, shippingCity=shippingCity, shippingState=shippingState, phone1=phone1, phone2=phone2, user=user)
       u.save()
       return redirect ('myAccount')
    else:
     upForm = UserAddressForm
    return render(request, 'profile.html', {'pform':upForm})

def displayAddress(request):
    
    a=UserAddress.objects.filter(user=request.user)
    return render (request, 'displayAddress.html', {'a':a})
def editAddress(request,addressId):
    instance=get_object_or_404(UserAddress, pk=addressId)
    if request.method=='POST':
        upForm = UserAddressForm(request.POST, instance)
        if upForm.is_valid():
           shippingAddress1=upForm.cleaned_data['shippingAddress1']
           shippingAddress2=upForm.cleaned_data['shippingAddress2']
           shippingCity=upForm.cleaned_data['shippingCity']
           shippingState=upForm.cleaned_data['shippingState']
           phone1=upForm.cleaned_data['phone1']
           phone2=upForm.cleaned_data['phone2']
           firstName=upForm.cleaned_data['firstName']
           lastName=upForm.cleaned_data['lastName']
           user=request.user
           u=UserAddress(shippingAddress1=shippingAddress1, shippingAddress2=shippingAddress2, shippingCity=shippingCity, shippingState=shippingState, firstName=firstName,lastName=lastName,phone1=phone1, phone2=phone2, user=user,pk=addressId)
           u.save()
           return redirect ('myAccount')
    else:
     upForm = UserAddressForm(instance=instance)
    return render(request, 'profile.html', {'pform':upForm})
        

def deleteAddress(request,addressId):
 a=get_object_or_404(UserAddress, pk=addressId)
 referer=request.session.get('referer')
 if request.method=='POST':
     if request.POST.get("yes"):     
       a.delete()
       return redirect(referer)
     elif request.POST.get("no"):                 
        return redirect(referer)
 else:
        referer=request.META.get('HTTP_REFERER')
        request.session['referer']=referer
        return render(request, 'deleteAddress.html')
        

def userInformation(request):
    user=request.user
    if request.method=='POST':
        uForm=UserForm(data=request.POST, instance=request.user)
        if uForm.is_valid():
            user.avatar=uForm.cleaned_data['avatar']
            user.first_name=uForm.cleaned_data['first_name']
            user.last_name=uForm.cleaned_data['last_name']
            user.dob=uForm.cleaned_data['dob']
            
            user.save()
            
            return redirect ('myAccount')
            
    else:
       uForm=UserForm(instance=user)
    return render(request,'userInformation.html', {'uForm':uForm})
            

def myAccount(request):

    return render (request, 'account.html')





