from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('main_app/', include("webapp.main_app.urls")),
    #path('', include ('main_app.urls')),
]
