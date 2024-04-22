from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from movieshow_app.views import *



urlpatterns =[

    path('dashboard/',MovieHome.as_view(),name='dashboard'),
     path('movie_filter/',MovieFilter.as_view(),name='movie_filter'),
    path('movie_details/', MovieView.as_view(),name='movie'),
    path('movie_details/<int:pk>', MovieView.as_view(),name='movie')



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)