# Generated by Django 2.2.3 on 2019-07-24 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kottayamhosters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_logo',
            name='name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]