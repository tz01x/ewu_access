# Generated by Django 4.0 on 2021-12-09 15:11

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.ImageUploderPath.uploadTo, verbose_name='Picture'),
        ),
        migrations.AlterField(
            model_name='community',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.ImageUploderPath.uploadTo, verbose_name='Picture'),
        ),
        migrations.AlterField(
            model_name='images',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.ImageUploderPath.uploadTo),
        ),
    ]
