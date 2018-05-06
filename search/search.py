from search.models import SearchTerm
from bookdetailsc.models import Book
from django.db.models import Q

##from ecomstore.stats import stats

STRIP_WORDS = ['a','an','and','by','for','from','in','no','not',
               'of','on','or','that','the','to','with']

def store(request, q):
    """ stores the search text """
    # if search term is at least three chars long, store in db
    if len(q) > 2:
        term = SearchTerm()
        term.q = q
        term.ip_address = request.META.get('REMOTE_ADDR')
##        term.tracking_id = stats.tracking_id(request)
        term.user = None
        if request.user.is_authenticated():
            term.user = request.user
        term.save()
    
def products(search_text):
    """ get products matching the search text """
    words = _prepare_words(search_text)
    
    books= Book.active.all()
    
    results = {}
    for word in words:
        books = books.filter(Q(name__icontains=word) |
        Q(bookDescription__icontains=word) |        
        Q(isbn__iexact=word)|
        Q(metaKeywords__icontains=word)|
        Q(slug__icontains=word)|
        Q(author__name__icontains=word)|
        Q(publisher__name__icontains=word))
        results['books'] = books
    print(results)
    return results
    
def _prepare_words(search_text):
    """ strip out common words, limit to 5 words """
    words = search_text.split()
    for common in STRIP_WORDS:
        if common in words:
            words.remove(common)
    return words[0:5]
