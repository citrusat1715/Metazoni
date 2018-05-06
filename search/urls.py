
from django.conf.urls import include, url
from search import views as searchview
urlpatterns = [

     url(r'^results',searchview.results, name='searchResults'),
]
