# Generated by Django 3.2.7 on 2021-09-17 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=100),
        ),
    ]
