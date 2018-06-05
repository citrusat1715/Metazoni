import re
from scrapy import Selector
from urllib.request import urlopen
from bookdetailsc.models import Category
from django.db import transaction
from django.shortcuts import get_object_or_404
def replacee(value):
    value=value.strip('"[]')
    value=value.strip("'")
    return value

def category_list():
    dicto={}
    listo=['918','876','881','330','906','917','170','931','940','163','169','172','921','184','185','187','1013','958','930','951','173','189']
    count=0
    for i in range(0,len(listo)):
     count+=1  
     url='http://www.libertybooks.com/index.php?route=product/category&path='+listo[i]+''
     html=urlopen(url).read()
     sel=Selector(text=html)
     topcat=sel.xpath('//*[@id="content"]/h1/text()').extract()
     subcat=sel.xpath('//*[@id="journal-super-filter-54"]/div[2]/div[2]/ul/li/label/a/span/text()').extract()
     if subcat:
        dicto.update({replacee(str(topcat)):''})
        for cat in subcat:
            parent=replacee(str(topcat))
            name=replacee(str(cat))
            dicto.update({name:parent})
            
     else:
         dicto.update({replacee(str(topcat)):''})


    return dicto

def create_objects():
    url='static/bookdetailsc/soimages/category/thumbnails/arts_fiml_and_photography_xeRbF8v.jpg'
    dicto=category_list()
    cato=[]
    obj=''

    for name,parent in dicto.items():
         slug=(re.sub(r'[^a-zA-Z]','',name))
         cato=Category(name=name, slug=slug,parent=None,description='added',isActive=True,
                          metaKeywords='addkey',metaDescription='addmeta',thumbnailImage=url)
         cato.save()
     
                            
