# Generated by Django 4.1.4 on 2023-03-21 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_rename_title_material_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='title',
            new_name='name',
        ),
    ]
