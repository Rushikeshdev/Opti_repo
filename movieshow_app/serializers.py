from rest_framework.serializers import ModelSerializer
from movieshow_app.models import *


class MovieSerializer(ModelSerializer):

    class Meta:
        model=Movie
        fields = '__all__'
