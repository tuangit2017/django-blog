# Generated by Django 2.2 on 2019-11-07 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='users/default.jpg', null=True, upload_to='users/%Y/%m/%d'),
        ),
    ]
