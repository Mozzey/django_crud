# Generated by Django 2.1.3 on 2018-11-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181117_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to='profile_pics'),
        ),
    ]
