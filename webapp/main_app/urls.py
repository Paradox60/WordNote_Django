from django.urls import path
from .views import home, page1, page2, page3

urlpatterns = [
   path('', home, name="home"),
   path('add_words/', page1, name='add_words'),
   path('test/', page2, name='test'),
   path('library/', page3, name='library'),
]
