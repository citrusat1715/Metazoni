
from metazon import settings
from accounts import views as accountview
from django.conf.urls import include, url
from django.contrib.auth.views import login,logout,password_reset,password_reset_done,password_reset_confirm,password_reset_complete



urlpatterns = [

    
    url(r'^customer/register',accountview.signup, name='registerUser'),
    url(r'^customer/login/$',login,{'template_name': 'registration/login.html',}, name='login'),
    url(r'^customer/logout/$',logout,{'template_name': 'registration/logout.html',}, name='logout'),
    url(r'^customer/password_reset/$', password_reset, name='passwordReset'),
    url(r'^customer/password_reset/done/$',password_reset_done, name='password_reset_done'),
    url(r'^customer/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',password_reset_confirm, name='password_reset_confirm'),
    url(r'^customer/password/reset/done/$', password_reset_complete, name='password_reset_complete'),
    url(r'^customer/account/$', accountview.myAccount, name='myAccount'),
    url(r'^customer/address/$' ,accountview.userAddress, name='addAddress'),
    url(r'^customer/address/index/$' ,accountview.displayAddress, name='displayAddress'),
    url(r'^customer/address/edit/(?P<addressId>[0-9]+)$' ,accountview.editAddress, name='editAddress'),
    url(r'^customer/address/delete/(?P<addressId>[0-9]+)$' ,accountview.deleteAddress, name='deleteAddress'),
    url(r'^customer/personalInformation' ,accountview.userInformation, name='userInformation'),
    
##    url(r'^order_info/$', accountview.orderInfo,{'template_name': 'registration/order_info.html'}, name='orderInfo'),
##    url(r'^order_details/(?P<order_id>[-\w]+)/$', accountview.orderDetail,{'template_name': 'registration/order_details.html'}, name='orderDetails'),
##)
    ]

##	    {'template_name': 'registration/register.html', 'SSL': settings.ENABLE_SSL }, 'register'),


	
