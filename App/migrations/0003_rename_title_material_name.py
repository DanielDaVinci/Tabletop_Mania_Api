# Generated by Django 4.1.4 on 2023-03-21 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_rename_meterials_game_materials_alter_game_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='title',
            new_name='name',
        ),
    ]
