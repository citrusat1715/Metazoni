from django.contrib import admin
from bookdetailsc.models import Category,Publisher,Author,Book,CondFormPrice
from mptt.admin import MPTTModelAdmin

# Register your models here.


class CondFormPriceInline(admin.TabularInline):
 model=CondFormPrice

class BookAdmin(admin.ModelAdmin):
 inlines=[CondFormPriceInline,]
 
class CustomMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20
admin.site.register(Category,CustomMPTTModelAdmin)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book,BookAdmin)
admin.site.register(CondFormPrice)

