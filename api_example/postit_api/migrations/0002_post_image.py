# Generated by Django 5.0.2 on 2024-03-05 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postit_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='post_images', verbose_name='image'),
        ),
    ]
