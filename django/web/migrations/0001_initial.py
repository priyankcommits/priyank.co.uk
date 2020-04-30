# Generated by Django 2.0.7 on 2018-08-04 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(default='', max_length=200)),
                ('text', models.CharField(default='', max_length=500)),
                ('link', models.CharField(default='', max_length=1000)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(default='', max_length=1000)),
                ('subheadline', models.CharField(default='', max_length=1000)),
                ('content', models.TextField(default='', max_length=100000)),
                ('image', models.CharField(default='', max_length=500)),
                ('likes', models.IntegerField(default=0)),
                ('kind', models.IntegerField(default=0)),
                ('upvote_value', models.IntegerField(default=0)),
                ('downvote_value', models.IntegerField(default=0)),
                ('upvote_label', models.CharField(default='Yes', max_length=200)),
                ('downvote_label', models.CharField(default='No', max_length=200)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('image', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=300, unique=True)),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='by',
            field=models.ForeignKey(on_delete=None, related_name='profile', to='web.Profile'),
        ),
    ]