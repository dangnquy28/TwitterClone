# Generated by Django 4.1.3 on 2022-12-19 01:35

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='Anonymous', max_length=140, verbose_name='Name')),
                ('body', models.CharField(blank=True, db_index=True, max_length=140, null=True, verbose_name='Body')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('created_at', models.DateTimeField(blank=True, verbose_name='Created Datetime')),
                ('likes', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='like count')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
