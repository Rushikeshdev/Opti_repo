from ntpath import join
from django.core.management.base import BaseCommand, CommandError
import requests,os
import random
from movieshow_app.models import *
from pathlib import Path
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

class Command(BaseCommand):


    def handle(self, *args, **options):

        
        BASE_URL = 'https://api.themoviedb.org/3'

        API_KEY = 'd962a21f9291adc93cfe547e80a0d8e0'

        
        all_movies = []
        page =1
        total_pages = float('inf')

        while page <= total_pages:

            url = f'{BASE_URL}/discover/movie'

            headers = {"accept": "application/json"}

            params = {'api_key': f'{API_KEY}'}

            response = requests.get(url, headers=headers,params=params)

            data = response.json()

            if total_pages == float('inf'):
                total_pages = data['total_pages']
            
            all_movies.extend(data['results'])

            print("page",page)
            page += 1

            if page == 50:
                break
       

        def fetch_genre_mapping():
            endpoint = f'{BASE_URL}/genre/movie/list'
            params = {'api_key': f'{API_KEY}'}
            response = requests.get(endpoint, params=params)
            data = response.json()
            genre_mapping = {genre['id']: genre['name'] for genre in data['genres']}
            return genre_mapping

        def add_genre_to_movie(movie, genre_mapping):
            genre_ids = movie.get('genre_ids', [])
            genres = [genre_mapping.get(genre_id, 'Unknown') for genre_id in genre_ids]
            movie['genres'] = genres
            return movie


       
        genre_mapping = fetch_genre_mapping()
        all_movies = [add_genre_to_movie(movie, genre_mapping) for movie in all_movies]


        def metacrictic_and_duration(movie):
           
            
            metacrictic_rating = [random.uniform(0,100) for _ in range(50)]
            for rating in metacrictic_rating:
                movie['metacrictic_rating'] = rating
            duration = [random.randint(1,3) for _ in range(50)]
            for duration in duration:
                movie['duration'] = duration
          
            return movie

        all_movies = [metacrictic_and_duration(movie) for movie in all_movies]

        def get_the_poster(poster_path):

            file_name = os.path.basename(poster_path)

            media_path = os.path.join('media', file_name)

            default_storage.save(media_path, ContentFile(response.content))

            return media_path

       

        def realmovie_data(all_movies):

            for movie in all_movies:

               
                

                poster_path = get_the_poster(movie['poster_path'])

                Movie.objects.create(title=movie['title'],
                  poster=poster_path,
                  genre=movie['genres'],
                  rating=movie['vote_average'],
                 
                  release_year=movie['release_date'][:4],
                  metacrictic_rating=movie['metacrictic_rating'],
                  runtime_movie=movie['duration'])

            self.stdout.write(
                self.style.SUCCESS('Successfully Fetch Movie Data')
            )

         

        realmovie_data(all_movies[1:50])

       




       
        
       

