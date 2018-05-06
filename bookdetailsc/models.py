from django.db import models
from django.forms import ModelForm
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language, pgettext_lazy
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
from django.shortcuts import get_object_or_404

class ActiveCategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isActive=True)

class Category(MPTTModel):
    name=models.CharField(max_length=50,blank=False,unique=True)
    slug=models.SlugField(max_length=50, unique=True, help_text='Unqiue value for product page URL, created from name.')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    description=models.TextField()
    isActive=models.BooleanField(default=True)
    metaKeywords=models.CharField("Meta Keywords", max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    metaDescription=models.CharField("Meta Description ", max_length=255, help_text='Content for desciption meta tag')
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)
    thumbnailImage=models.FileField(upload_to='static/bookdetailsc/soimages/category/thumbnails',blank=False)

    objects=models.Manager()
    active=ActiveCategoryManager()

    class MPTTMeta:
        order_insertion_by = ['name']
    

    class Meta:
        db_table='categories'
        
        verbose_name_plural='Categories'
        ordering=['pk']
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
  
     return reverse('viewCategory', kwargs={'slug':self.slug})

    def get_edit_url(self):  
     return reverse('editCategory', kwargs={'slug': self.slug})
    
    def get_delete_url(self):  
     return reverse('deleteCategory', kwargs={'slug': self.slug})
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name=models.CharField(max_length=50, blank=False, unique=False)
    
    popularity=models.CharField(max_length=10,blank=True,unique=False)
    contact=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return (self.name)
    def get_absolute_url(self):
  
     return reverse('viewAuthor', kwargs={'authorId':self.id})

    def get_edit_url(self):  
     return reverse('mobiles-edit', kwargs={'product_id': self.id})
    
    def get_delete_url(self):  
     return reverse('mobiles-delete', kwargs={'product_id': self.id})
class Publisher(models.Model):
    name=models.CharField(max_length=50, blank=False, unique=False)
    address=models.CharField(max_length=50, blank=True)
    contact=models.CharField(max_length=50, blank=True)
    dealTerms=models.CharField(max_length=50,blank=True)
    otherInformation=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return (self.name)
    

    def get_absolute_url(self):
  
     return reverse('viewPublisher', kwargs={'publisherId':self.id})

    def get_edit_url(self):  
     return reverse('mobiles-edit', kwargs={'product_id': self.id})
    
    def get_delete_url(self):  
     return reverse('mobiles-delete', kwargs={'product_id': self.id})    

class ActiveBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(inStock=True)
class Book(models.Model):
    Urdu,English,Punjabi, Pashto,Arabic, Sindhi='Urdu','English','Punjabi','Pashto','Arabic','Sindhi'
    languageChoices=(
        (Urdu,('Urdu')),
        (English,_('English')),
        (Punjabi,_('Punjabi')),
        (Pashto,_('Pashto')),
        (Arabic,_('Arabic')),
        (Sindhi,_('Sindhi')),
        )
    name=models.CharField(max_length=255,unique=False)
    author=models.ManyToManyField(Author,blank=False)
    publisher=models.ForeignKey(Publisher,blank=False)
    isbn=models.CharField(max_length=20,blank=False)
    slug=models.SlugField(max_length=255,unique=False,help_text='Unqie value for product page URL,created from name')    
    sku=models.CharField(max_length=50)
    category=models.ForeignKey(Category, blank=False)    
    inStock=models.BooleanField(default=True)
    bookDescription=models.TextField(max_length=500,help_text='Overview of the Book')
    language=models.CharField(max_length=50,choices=languageChoices)
    metaKeywords=models.CharField("Meta Keywords", max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    metaDescription=models.CharField("Meta Description ", max_length=255, help_text='Content for desciption meta tag')
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)
    thumbnailImage=models.FileField(upload_to='images/book/thumbnail',blank=True)
    coverImage=models.FileField(upload_to='images/book/cover')
    preview=models.FileField(upload_to='bookPreview',blank=True)

    objects=models.Manager()
    active=ActiveBookManager()

    def __str__(self):
        return (self.name)
    def get_absolute_url(self):  
     return reverse('viewBook', kwargs={'bookId': self.id})

    def get_edit_url(self):  
     return reverse('editBook', kwargs={'bookId': self.id})

    def get_delete_url(self):  
     return reverse('deleteBook', kwargs={'bookId': self.id})

    def get_preview_url(self):
        return reverse('previewBook', kwargs={'bookId':self.id})
    @property
    def get_sellingPrice(self):
        b=get_object_or_404(CondFormPrice, book=self)
        return (b.sellingPrice)
    @property
    def get_purchasePrice(self):
        b=get_object_or_404(CondFormPrice,book=self)
        return (b.purchasePrice)
    @property
    def get_bookFormat(self):
        b=get_object_or_404(CondFormPrice,book=self)
        return (b.bookFormat)
    @property
    def get_bookCondition(self):
        b=get_object_or_404(CondFormPrice,book=self)
        return (b.bookCondition)

    
        

   
class CondFormPrice(models.Model):                              #condition+formating+price+dimesnion+weight
    New, Old, hardCover,paperBack='New','Old','HardCover','PaperBack'
    
    book=models.ForeignKey(Book,blank=False)
    conditionChoices=(                                          
        (New,_('New')),
        (Old,_('Old')))
    formatChoices=(
        (hardCover,_('HardCover')),
        (paperBack,_('PaperBack')),)
    
    bookFormat=models.CharField(max_length=20, choices=formatChoices,blank=False)
    bookCondition=models.CharField(max_length=20,choices=conditionChoices,blank=False)
    purchasePrice=models.CharField(max_length=5,blank=False)
    sellingPrice=models.CharField(max_length=5,blank=False)
    dimension=models.CharField(max_length=10,blank=True)
    weight=models.CharField(max_length=10, blank=True)

    def get_sellingPrice(self):
        return (self.sellingPrice)
    def get_bookFormat(self):
        return(self.bookFormat)
    def get_bookCondition(self):
        return(self.bookCondition)
    def get_dimension(self):
        return(self.dimension)
    def get_weight(self):
        return(self.weight)

    def get_absolute_url(self):
        return()
        

    def __str__(self):
        return('Condition:' + self.bookCondition +' Format:' +self.bookFormat + ' Price:'+self.sellingPrice )


    
    
