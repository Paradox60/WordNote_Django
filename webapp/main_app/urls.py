from django.urls import path
from .views import *


urlpatterns = [
   path('', home, name="home"),
   path('add_words/', add_words, name='add_words'),
   path('library/', library, name='library'),
   path('test/', test, name='test'),
   path('test_reverse/', test_reverse, name='test_reverse'),
   path('save_changes/', save_changes, name='save_changes'),
   path('delete_word_pair/', delete_word_pair, name='delete_word_pair'),
   path('change_progress/', change_progress, name='change_progress'),
   path('options/', options, name='options'),
   path('trying/', trying, name='trying'),
]

