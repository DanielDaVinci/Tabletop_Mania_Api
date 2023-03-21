from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse, Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models
from . import serializers


def get_image(request, name: str):
    try:
        img = open(f'uploads/images/{name}', 'rb')
    except:
        raise Http404
    response = FileResponse(img)
    return response


@api_view(['GET'])
def materials_get_range(request, start: int, end: int):
    if request.method == 'GET':
        materials = models.Material.objects.get_all_in_range(start, end)
        serializer_data = serializers.MaterialSerializer(materials, context={'request': request}, many=True)
        return Response({
            'data': serializer_data.data
        }, status=200)


@api_view(['GET'])
def material_get_by_id(request, id: int):
    if request.method == 'GET':
        material = models.Material.objects.find_by_id(id)
        serializer_data = serializers.MaterialSerializer(material, context={'request': request}, many=True)
        return Response({
            'data': serializer_data.data
        }, status=200)


@api_view(['GET'])
def game_get_by_id(request, id: int):
    if request.method == 'GET':
        game = models.Game.objects.find_by_id(id)
        serializer_data = serializers.GameSerializer(game, context={'request': request}, many=True)
        return Response({
            'data': serializer_data.data
        }, status=200)
