Project Name:

The Movies@Mariana


Description:
Mariana Tek there is showing the movies details.By using mariana tek we can get movies deatils like vice.

Title
Poster
Genre(s)
Rating
Year Release
Metacritic Rating
Runtime

There is one genre filter is provided by using this we can filter movie and also we can search movie used with movie title.

Prerequisites:
Python 3.8.10

Installation:

Step 1 : Create Virtual Env = python3 -m venv env_name

Step 2 : Install requirements = pip3 install requirements.txt

Step 3 : Do Migrations : python3 manage.py makemigrations
Step 4 : Made Migratre : python3 manage.py migrate

Step 5 : CreateSuper User: python3 manage.py createsuperuser
Step 6 : collect static media: python3 manage.py collectstatic

step 7 : collect movie data :python3 manage.py movie_data

step 8: start server: python3 manage.py runserver
