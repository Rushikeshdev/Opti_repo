
from django.shortcuts import render
from rest_framework import status
from movieshow_app.models import Movie
from django.views import View
from django.http.response import JsonResponse
import json



class MovieView(View):

    def get(self,request):

        try:
            movies = Movie.objects.all()
            genre = request.GET.get('genre')
            search_title = request.GET.get('title')
            
            if genre:

                movies = movies.filter(genre__contains=genre)

            elif search_title:
               
                movies = movies.filter(title__icontains=search_title)
    
           
            return render(request,template_name='movie.html',context={'movies':movies})

            
        except Exception as e:
            
            return Response("Bad Request"+ (e),status=status.HTTP_400_BAD_REQUEST)

    






    