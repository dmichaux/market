# Generated by Django 2.1.3 on 2018-11-15 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0006_auto_20181114_1457'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='img_url',
        ),
    ]
