# Generated by Django 2.2.3 on 2019-07-26 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kottayamhosters', '0003_add_design_add_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_design',
            old_name='description_logo',
            new_name='design_description_logo',
        ),
        migrations.RenameField(
            model_name='add_design',
            old_name='name',
            new_name='design_name',
        ),
        migrations.RenameField(
            model_name='add_design',
            old_name='photo',
            new_name='design_photo',
        ),
        migrations.RenameField(
            model_name='add_video',
            old_name='description_logo',
            new_name='video_description_logo',
        ),
        migrations.RenameField(
            model_name='add_video',
            old_name='name',
            new_name='video_name',
        ),
        migrations.RenameField(
            model_name='add_video',
            old_name='photo',
            new_name='video_photo',
        ),
    ]
