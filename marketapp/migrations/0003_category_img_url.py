# Generated by Django 2.1.3 on 2018-11-14 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0002_auto_20181113_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img_url',
            field=models.URLField(default='https://images.pexels.com/photos/210557/pexels-photo-210557.jpeg?cs=srgb&dl=buildings-business-city-210557.jpg&fm=jpg'),
        ),
    ]
