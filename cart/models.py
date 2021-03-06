from django.db import models
from bookdetailsc.models import Book

# Create your models here.
class CartItem(models.Model):
  cart_id = models.CharField(max_length=50)
  date_added = models.DateTimeField(auto_now_add=True)
  quantity = models.IntegerField(default=1)
  book = models.ForeignKey('bookdetailsc.Book', unique=False)

  class Meta:
   db_table = 'cart_items'
   ordering = ['date_added']
  def total(self):
    return self.quantity * 1
  def name(self):
    return self.book.name
  def price(self):
   return self.book.get_sellingPrice

  def get_absolute_url(self):
    return self.book.get_absolute_url()
  def augment_quantity(self, quantity):
    self.quantity = self.quantity + int(quantity)
    self.save()
    
