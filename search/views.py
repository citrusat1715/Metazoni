from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from search import search
from metazon import settings

##from django.utils import simplejson
from django.http import HttpResponse
from django.core import serializers
from bookdetailsc.models import Book

def results(request, template_name="results.html"):
    
    """ template for displaying settings.PRODUCTS_PER_PAGE paginated product results """
    # get current search phrase
    q = request.GET.get('q', '')
    matching = search.products(q).get('books', [])
    
   
#---------------------pagination------------------------------------------------#

    try:
        page = int(request.GET.get('page', 1))## page number goes here
    except ValueError:
        page = 1   
    paginator = Paginator(matching,settings.BOOKS_PER_PAGE)    
    try:
        results = paginator.page(page).object_list
    except (InvalidPage, EmptyPage):
        results = paginator.page(1).object_list        
#-----------------------------------------------------------------------------#

    search.store(request, q)    
    page_title = 'Search Results for: ' + q
    context=locals()
    return render(request,template_name, context)
##def results(request, template_name="results.html"):
##    
##    """ template for displaying settings.PRODUCTS_PER_PAGE paginated product results """
##    # get current search phrase
##    q = request.GET.get('q', '')
##    matching = search.products(q).get('books', [])
##    try:
##    page=request.Get.get('page',1) ##page number here
##    except ValueError:
##        page=1
##    paginator=Paginator(matching,
##
##        
##    
##    paginator = Paginator(matching,2)    
##    try:
##        results = paginator.page(page).object_list
##    except (InvalidPage, EmptyPage):
##        results = paginator.page(1).object_list        
##    search.store(request, q)    
##    page_title = 'Search Results for: ' + q
##    context=locals()
##    return render(request,template_name, context)
