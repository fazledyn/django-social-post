# Generated by Django 3.0.7 on 2020-06-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0005_auto_20200611_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
    ]
