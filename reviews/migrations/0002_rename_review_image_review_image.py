# Generated by Django 3.2.13 on 2022-11-10 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_image',
            new_name='image',
        ),
    ]
