from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from movieshow_app.models import Movie
from movieshow_app.serializers import MovieSerializer
from django.views import View
from django.http.response import JsonResponse
import json
from django.core.serializers import serialize



# Create your views here.

class MovieHome(View):

    def get(self,request):


        movie = Movie.objects.all()

        genre = request.GET.get('genre')


        if genre:

            movie = movie.filter(genre=genre)



        return render(request,'movie.html',context={'movie':movie})


class MovieFilter(View):

    def get(self,request):


        movie = Movie.objects.all()

        genre = request.GET.get('genre')
        title = request.GET.get('title')


        if genre:
           
            movie = movie.filter(genre__contains=genre)
            
        if title:
             
            movie = movie.filter(title=title)

        

        # return render(request,'movie.html',context={'movie':movie})

        return JsonResponse(data=movie,status=200,safe=False)



class MovieView(APIView):

    def post(self,request):

        serializer = MovieSerializer(data=request.data)


        try:
            if serializer.is_valid():

                serializer.save()

                return Response("Message:Movie Created Successfully",status=status.HTTP_201_CREATED)

            return Response("Error:Something went to wrong",serializer.errors)

        except:

            return Response("Error:Internal Server Error",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    def  get_object(self,pk):

        try:

            movie_instance = Movie.objects.get(pk=pk)
            return movie_instance
        except Movie.DoesNotExist:
            return None


    def get(self,request,pk=None):

        try:
            if pk is not None:
                movie_instance = self.get_object(pk)

                if movie_instance is None:

                   return Response("Message:Resource Not Found",status=status.HTTP_404_NOT_FOUND)

                serilizer = MovieSerializer(movie_instance)

                return Response(serilizer.data,status=status.HTTP_200_OK)

            all_movies = Movie.objects.all()

            serilizer = MovieSerializer(all_movies,many=True)

            return Response(serilizer.data,status=status.HTTP_200_OK)
        except:
            
            return Response("Bad Request",status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):


        try:
            movie_instance = self.get_object(pk)
            

            if movie_instance is None:

                return Response("Message:Resource Not Found",status=status.HTTP_404_NOT_FOUND)
            
            serilizer = MovieSerializer(movie_instance,data=request.data, partial=True)

           
            if serilizer.is_valid():

                serilizer.save()

                return Response("Message:Movie Updated Successfully",status=status.HTTP_200_OK)
        
            return Response("Internal Server Error",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:

            return Response("Bad Request",status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        try:
                movie_instance = self.get_object(pk)

                if movie_instance is None:
                            return Response({"detail": "Resource not found."},
                                            status=status.HTTP_404_NOT_FOUND)

                movie_instance.delete()
                return Response({"message": "Resource deleted successfully."},
                            status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)






    