# Generated by Django 4.2.2 on 2023-07-05 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_alter_team_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
