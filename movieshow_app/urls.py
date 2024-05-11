from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from movieshow_app.views import *



urlpatterns =[

    
    path('', MovieView.as_view(),name='movie'),
    



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)