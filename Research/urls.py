from django.urls import path
from .views import BookView,IndiBookView,IndiSpecificBookView,PersonView,AuthorView,EditorView,NovelListView,BaseAuthorsView,AvailableAuthorsView

urlpatterns = [
    path('view/', BookView.as_view(), name='book-view'),
    path('indiview/', IndiBookView.as_view(), name='indibook-view'),
    path('indibooks/specific/', IndiSpecificBookView.as_view(), name='indi-specific-book-view'),
    path('personview/', PersonView.as_view(), name='person-view'),
    path('authorview/', AuthorView.as_view(), name='author-view'),
    path('editorview/', EditorView.as_view(), name='editor-view'),
    path('authors/available/', AvailableAuthorsView.as_view(), name='available-authors'),
    path('novels/', NovelListView.as_view(), name='book-list'),
    path('baseAuthor/', BaseAuthorsView.as_view(), name='base-author'),
]