from django.shortcuts import render
from bookdetailsc.forms import categoryForm,publisherForm,authorForm,bookForm,cfpForm,ProductAddToCartForm
from bookdetailsc.models import Category,Publisher,Author,Book,CondFormPrice
from django.shortcuts import get_object_or_404, render_to_response
from django.shortcuts import render, redirect
from bookdetailsc.helpers import grouped
from django.forms import formset_factory
from django.db import transaction

from django.db import IntegrityError
from cart import cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
##@login_required(login_url='/metazon/user/login')
def addCategory(request,template_name='addCategory.html'):

    User=get_user_model()
    print(User.objects.all())
        
    if request.method=='POST':

            form=categoryForm(request.POST or None,request.FILES)
            if form.is_valid():
             form=form.save(commit=True)
            else:
               print(form.errors)
               return render(request,'addCategory.html',{'form':form.data})



    form = categoryForm()
    return render(request,'addCategory.html',{'form':form})
def viewCategory(request,slug):
    
    c=get_object_or_404(Category, slug=slug)
    
    

    if c:
        context={}

        if c.is_root_node():
            childcats=c.get_children()            
            count=childcats.count()                                    
            books=(Book.objects.filter(category__in=childcats))
            if books:
              
              books=grouped(books,4)
        else:
            books=Book.objects.filter(category=c)
            if books:           
              books=grouped(books,4)        
        if not c.is_leaf_node():            
            count=c.get_children().count()           
            if count>0:
                if count>=6:                
                 object_list = grouped(c.get_children().order_by('pk'),6)
                 context={'object_list':object_list,
                          'books':books}
                if count<6:
                 objects=c.get_children()
                 context={'objects':objects,
                          'books':books}                                         
        if c.is_leaf_node():
            books=Book.objects.filter(category=c)
            if books:             
              books=grouped(books,4)                  
            objecto='none'            
            context={'objecto':objecto,
                          'books':books
                     }
            print(books)
    return render(request,'showCategory.html',context)
    
def viewCategories(request):
  
    
   
    context = {}
    context['object_list'] = grouped(Category.objects.all().order_by('pk'),6)    
    return render_to_response('showCategories.html', context)  ##can also be done using viewcategory template

def deleteCategory(request, slug,template_name='deletecategory.html'):    
    category = get_object_or_404(Category, slug=slug)   
    if request.method=='POST':
        
        print(Category.objects.all())
        Book.objects.filter(category=category).delete()
        category.delete()
        print(Book.objects.all())
        print(Category.objects.all())
      
        referer=request.session.get('referer')
        return redirect(referer)
    else:
        referer=request.META.get('HTTP_REFERER')
        request.session['referer']=referer
    return render(request, template_name, {'category':category})

def editCategory(request,slug):
     if request.method== 'POST':       
            instance = get_object_or_404(Category, slug=slug)
            form = categoryForm(request.POST or None,request.FILES, instance=instance)
            
            if form.is_valid():  #is_valid is function not property                       
             form = form.save(commit=True)
             return redirect('viewCategory' ,slug)
     else:
            instance = get_object_or_404(Category, slug=slug)
            form = categoryForm(instance=instance)
     return render(request,'editCategory.html',{'form':form})

def addPublisher(request,template_name='addPublisher.html'):    
    if request.method=='POST':
        
            form=publisherForm(request.POST)
            if form.is_valid():
             form=form.save(commit=True)
            else:
               print(form.errors)
               return render(request,'addPublisher.html',{'form':form.data})

    form = publisherForm()
    return render(request,'addPublisher.html',{'form':form})

def viewPublisher(request, publisherId):
    p=get_object_or_404(Publisher, pk=publisherId)   
    return render(request,'viewCategory.html',{'p':p})

def viewPublishers(request, template_name='viewPublishers.html'):
    p=Publisher.objects.all()
    for objects in p:
        print(objects.name)
    return render(request,'viewPublishers.html',{'p':p})

def addAuthor(request,template_name='addAuthor.html'):    
    if request.method=='POST':
        
            form=authorForm(request.POST)
            if form.is_valid():
             form=form.save(commit=True)
            else:
               print(form.errors)
               return render(request,'addAuthor.html',{'form':form.data})

    form = authorForm()
    return render(request,'addAuthor.html',{'form':form})

def viewAuthor(request, authorId):
    a=get_object_or_404(Author, pk=authorId)   
    return render(request,'viewCategory.html',{'a':a})

def viewAuthors(request,template_name='viewAuthors.html'):
    a=Author.objects.all()
    return render(request,'viewAuthors.html',{'a':a})

def addBook(request,template_name='cfpbookdemo.html'):    
    if request.method=='POST':
            
        
            form=bookForm(request.POST or None,request.FILES)
            cfpform=cfpForm(request.POST or None)
            print(form.data)
            print(cfpform.data)
            if form.is_valid() and cfpform.is_valid():             
             form=form.save(commit=True)
             book=form
             bookFormat = cfpform.cleaned_data.get('bookFormat')
             bookCondition = cfpform.cleaned_data.get('bookCondition')
             sellingPrice = cfpform.cleaned_data.get('sellingPrice')
             purchasePrice = cfpform.cleaned_data.get('purchasePrice')
             dimension = cfpform.cleaned_data.get('dimension')
             weight = cfpform.cleaned_data.get('weight') 
             cfp=CondFormPrice(bookFormat=bookFormat,bookCondition=bookCondition,sellingPrice=sellingPrice,purchasePrice=purchasePrice,dimension=dimension,weight=weight,book=book)
             cfp.save()
            else:
               form=bookForm(form.data)
               cfpform=cfpForm(cfpform.data)

               return render(request,'cfpbookdemo.html',{'form':form, 'cfpform':cfpform})

    form = bookForm()
    cfpform=cfpForm()
    return render(request,'cfpbookdemo.html',{'form':form, 'cfpform':cfpform})

def viewBook(request, bookId):
    
    
    b=get_object_or_404(Book, pk=bookId)
    print(b.author.all())


    author=b.author.all()
    p=b.get_preview_url()
    if request.method == 'POST':       
        #create the bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        #check if posted data is valid
        if form.is_valid():
            #add to cart and redirect to cart page
            cart.add_to_cart(request)
            # if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            
            return redirect('viewCart')
    else:
        #create the unbound form. Notice the request as a keyword argument
        form = ProductAddToCartForm(request=request, label_suffix=':')
    # assign the hidden input the product slug
    form.fields['pk'].widget.attrs['value'] = b.pk
    # set test cookie to make sure cookies are enabled
    request.session.set_test_cookie()
    return render(request,'displaybook.html',{'book':b,'a':author,'p':p,'form':form})

def viewBooks(request):
    
    context = {}
    context['object_list'] = grouped(Book.active.all().order_by('pk'),6)
    
    
    return render_to_response('showbooksdemo.html', context)
    
def deleteBook(request, bookId,template_name='deleteBook.html'):    
    book = get_object_or_404(Book, pk=bookId)   
    if request.method=='POST':
        book.delete()      
        referer=request.session.get('referer')
        return redirect(referer)
    else:
        referer=request.META.get('HTTP_REFERER')
        request.session['referer']=referer
    return render(request, template_name, {'book':book})

def editBook(request,bookId):
    instance=get_object_or_404(Book,pk=bookId)
    cfp=get_object_or_404(CondFormPrice,book=instance)
    if request.method=='POST':
            form=bookForm(request.POST or None,request.FILES,instance=instance)
            cfpform=cfpForm(request.POST or None,request.FILES,instance=cfp)            
            if form.is_valid() and cfpform.is_valid():             
             form=form.save(commit=True)
             cfpform.save()
            else:
               form=bookForm(form.data)
               cfpform=cfpForm(cfpform.data)
               return render(request,'cfpbookdemo.html',{'form':form, 'cfpform':cfpform})

    form = bookForm(instance=instance)

    cfpform=cfpForm(instance=cfp)
    return render(request,'cfpbookdemo.html',{'form':form, 'cfpform':cfpform})

             
     

def addbookcfp(request):
   CFPFormset=formset_factory(cfpForm)

   if request.method=='POST':
        form=bookForm(request.POST,request.FILES or None)
        cfpFormset = CFPFormset(request.POST,request.FILES)  
        if form.is_valid() and cfpFormset.is_valid():                           
            book=form.save(commit=True)            
            new_cfp = []
            for cfp in cfpFormset:
                book=book
                bookFormat = cfp.cleaned_data.get('bookFormat')
                bookCondition = cfp.cleaned_data.get('bookCondition')
                sellingPrice = cfp.cleaned_data.get('sellingPrice')
                purchasePrice = cfp.cleaned_data.get('purchasePrice')
                dimension = cfp.cleaned_data.get('dimension')
                weight = cfp.cleaned_data.get('weight') 
                new_cfp.append(CondFormPrice(book=book, bookFormat= bookFormat, bookCondition=bookCondition,sellingPrice=sellingPrice, purchasePrice=purchasePrice,dimension=dimension, weight=weight))

            
            with transaction.atomic():
                    #Replace the old with the new
##                    UserLink.objects.filter(user=user).delete()
                    CondFormPrice.objects.bulk_create(new_cfp)

                    # And notify our users that it worked
                    print('success')

            
            
##            return redirect('product-images-mobile')
        
        else:
            print(form.errors)
            return render(request,'cfpbookdemo.html',{'form':bookForm(form.data),'cfpForm':CFPFormset(cfpFormset.data)})
        
   return render(request,'cfpbookdemo.html',{'form':bookForm,'cfpForm':CFPFormset})


def previewBook(request, bookId):
    b=get_object_or_404(Book, pk=bookId)
    preview=b.preview.url

    return render(request,'previewBook.html',{'preview':preview})
    
    

