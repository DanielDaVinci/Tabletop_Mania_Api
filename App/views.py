from django.core.files.storage import FileSystemStorage
from django.http import FileResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core import settings
from . import serializers, models
from .models import Upload


# def get_image(request, name: str):
#     try:
#         img = open(f'uploads/images/{name}', 'rb')
#     except:
#         raise Http404
#     response = FileResponse(img)
#     return response


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

def image_upload(request):
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        image_type = request.POST['image_type']
        if settings.USE_S3:
            upload = Upload(file=image_file)
            upload.save()
            image_url = upload.file.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
        return render(request, 'upload.html', {
            'image_url': image_url
        })
    return render(request, 'upload.html')
