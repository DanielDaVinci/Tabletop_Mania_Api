from rest_framework import serializers

from App.models import *


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'
