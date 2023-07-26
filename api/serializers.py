from rest_framework.serializers import ModelSerializer
from .models import Anime, Studio


class AnimeSerializer(ModelSerializer):
    class Meta:
        model = Anime
        fields = "__all__"

class StudioSerializer(ModelSerializer):
    class Meta:
        model = Studio
        fields = "__all__"
