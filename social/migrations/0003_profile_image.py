# Generated by Django 3.1.7 on 2021-05-21 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20210521_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='sonido.jpg', upload_to=''),
        ),
    ]
