from rest_framework import serializers

from App.models import *


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

    def get_image_url(self, obj):
        request = self.context.get('request')
        image_url = obj.fingerprint.url
        return request.build_absolute_uri(image_url)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
