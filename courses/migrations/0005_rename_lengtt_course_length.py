# Generated by Django 3.2.7 on 2021-09-17 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_video_video_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='lengtt',
            new_name='length',
        ),
    ]
