# Generated by Django 4.0.3 on 2022-03-11 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='slug',
            field=models.SlugField(default='none'),
            preserve_default=False,
        ),
    ]
