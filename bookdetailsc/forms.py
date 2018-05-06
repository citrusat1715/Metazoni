from bookdetailsc.models import Category,Author,Publisher, Book, CondFormPrice
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError 
from django import forms
import re
from django.forms import formset_factory
##from catalogue.cleanfuncs import clean_get_digits_alphabets
from django.forms.models import inlineformset_factory
from mptt.forms import TreeNodeChoiceField,TreeNodeMultipleChoiceField

class categoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','slug','parent','description','isActive','metaKeywords','metaDescription','thumbnailImage']
        labels={
            'name':_('CategoryName'),
            'parent':_('Parent Category'),
            'slug':_('Slug'),
            'description':_('Description'),
            'isActive':_('IsActive'),
            'metaKeywords':_('MetaKeywords'),
            'metaDescription':_('MetaDescription'),
            'thumbnailImage':_('thumbnailImage'),
           
            }
        help_texts={
            'name':_('Choose Category Name'),
            'parent':_('Enter the closest parent'),
            'slug':_('Slug'),
            'description':_('Description of the category in few words'),
            'isActive':_('IsActive'),
            'metaKeywords':_('Keywords for SEO purpose'),
            'metaDescription':_('Description for SEO purpose'),
            'createdAt':_('Created On'),
            'updatedAt':_('Updated At'),
            'thumbnailImage':_('Thumbnail Image')
            }

class authorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=['name','popularity','contact']
##        thumbnailimage
        labels={
            'firstName':_('First Name'),
            'lastName':_('Last Name'),
            'contact':_('Contact'),
            'popularity':_('Popularity'),
            }

class publisherForm(forms.ModelForm):
        class Meta:
            model=Publisher
            fields=['name','address','contact','dealTerms','otherInformation']
            labels={
                'name':_('Publisher Name'),
                'address':_('Publisher Address'),
                'contact':_('Publisher Contact'),
                'otherInformation':_('Other Related Information'),
                }
class cfpForm(forms.ModelForm):##form for the class CondFormPrice =Condition, Formating Price

   class Meta:
            model=CondFormPrice
            fields=['bookFormat','bookCondition','purchasePrice','sellingPrice','dimension','weight']
            labels={
             
                'bookFormat':_('Book Format'),
                'bookCondition':_('Condition'),
                'purchasePrice':_('Purchase Price'),
                'sellingPrice':_('Selling price'),
                'dimension':_('Dimension'),
                'weight':_('Weight'),
                }
            
                    

class bookForm(forms.ModelForm):

    category = TreeNodeChoiceField(queryset=Category.objects.all())
    author=forms.ModelMultipleChoiceField(
                                         queryset=Author.objects.all())
    class Meta:

     model=Book
     fields=['name','author','publisher','isbn','slug','sku','category','inStock','language','bookDescription','metaKeywords','metaDescription','thumbnailImage','preview','coverImage']
                
     labels={
         'name':_('Book Name'),
         'author':_('Author'),
         'publisher':_('Publisher'),
         'isbn':_('ISBN'),
         'slug':_('Slug'),
         'sku':_('SKU'),
         'category':_('Category'),
         'inStock':_('InStock'),
         'language':_('Language'),         
         'bookDescription':_('Book Description'),
         'metaKeywords':_('Meta Keywords'),
         'metaDescription':_('Meta Description'),
         'createdAt':_('CreatedAt'),
         'updatedAt':_('UpdatedAt'),
         'thumbnailImage':_('thumbnailImage'),
         'coverImage':_('coverImage'),
         'preview':_('preview'),
         }

class ProductAddToCartForm(forms.Form):
    """ form class to add items to the shopping cart """
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'size':'2', 'value':'1', 'class':'quantity'}), 
                                  error_messages={'invalid':'Please enter a valid quantity.'}, 
                                  min_value=1)
    pk = forms.CharField(widget=forms.HiddenInput())
    
    def __init__(self, request=None, *args, **kwargs):
        """ override the default so we can set the request """
        self.request = request
        super(ProductAddToCartForm, self).__init__(*args, **kwargs)
    
    def clean(self):
        """ custom validation to check for presence of cookies in customer's browser """
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError("Cookies must be enabled.")
        return self.cleaned_data
