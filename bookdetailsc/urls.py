
from metazon import settings
from bookdetailsc import views as bookviews
from django.conf.urls import include, url




urlpatterns = [
    url(r'^category/add',bookviews.addCategory,name='addCategory'),
    url(r'^categories',bookviews.viewCategories,name='viewCategories'),
    url(r'^category/(?P<slug>\w+)$',bookviews.viewCategory,name='viewCategory'),
    url(r'^category/(?P<slug>\w+)/delete',bookviews.deleteCategory,name='deleteCategory'),
    url(r'^category/(?P<slug>\w+)/edit',bookviews.editCategory,name='editCategory'),    
    url(r'^publisher/add',bookviews.addPublisher,name='addPublisher'),
    url(r'^publishers',bookviews.viewPublishers,name='viewPublishers'),
    url(r'^publisher/(?P<publisherId>[0-9]+)',bookviews.viewPublisher,name='viewPublisher'),
    url(r'^author/add',bookviews.addAuthor,name='addAuthor'),
    url(r'^authors',bookviews.viewAuthors,name='viewAuthors'),
    url(r'^author/(?P<authorId>[0-9]+)',bookviews.viewAuthor,name='viewAuthor'),
    url(r'^book/add/',bookviews.addBook,name='addBook'),
    url(r'^books',bookviews.viewBooks,name='viewBooks'),
    url(r'^book/(?P<bookId>[0-9]+)$',bookviews.viewBook,name='viewBook'),
    url(r'^book/(?P<bookId>[0-9]+)/delete',bookviews.deleteBook,name='deleteBook'),
    url(r'^book/(?P<bookId>[0-9]+)/edit',bookviews.editBook,name='editBook'),

    url(r'^book/preview/(?P<bookId>[0-9]+)',bookviews.previewBook,name='previewBook'),    
    ]

