from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read-write'
    file_overwrite = True

class MaterialStorage(S3Boto3Storage):
    location = 'media/material/'
    default_acl = 'public-read-write'
    file_overwrite = True

class GameStorage(S3Boto3Storage):
    location = 'media/game/'
    default_acl = 'public-read-write'
    file_overwrite = True