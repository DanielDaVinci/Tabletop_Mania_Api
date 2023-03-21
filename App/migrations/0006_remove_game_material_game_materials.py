# Generated by Django 4.1.4 on 2023-03-21 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_rename_materials_game_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='material',
        ),
        migrations.AddField(
            model_name='game',
            name='materials',
            field=models.ManyToManyField(blank=True, related_name='materials', to='App.material'),
        ),
    ]
