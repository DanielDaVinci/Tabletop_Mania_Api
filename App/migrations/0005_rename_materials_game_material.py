# Generated by Django 4.1.4 on 2023-03-21 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_rename_title_game_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='materials',
            new_name='material',
        ),
    ]