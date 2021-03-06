# Generated by Django 3.1.2 on 2020-10-05 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=200)),
                ('Year', models.CharField(blank=True, max_length=200)),
                ('Rated', models.CharField(blank=True, max_length=200)),
                ('Released', models.CharField(blank=True, max_length=200)),
                ('Runtime', models.CharField(blank=True, max_length=200)),
                ('Genre', models.CharField(blank=True, max_length=200)),
                ('Director', models.CharField(blank=True, max_length=200)),
                ('Writer', models.CharField(blank=True, max_length=200)),
                ('Actors', models.CharField(blank=True, max_length=200)),
                ('Plot', models.CharField(blank=True, max_length=200)),
                ('Language', models.CharField(blank=True, max_length=200)),
                ('Country', models.CharField(blank=True, max_length=200)),
                ('Awards', models.CharField(blank=True, max_length=200)),
                ('Poster', models.CharField(blank=True, max_length=200)),
                ('Ratings', models.CharField(blank=True, max_length=200)),
                ('Metascore', models.CharField(blank=True, max_length=200)),
                ('imdbRating', models.CharField(blank=True, max_length=200)),
                ('imdbVotes', models.CharField(blank=True, max_length=200)),
                ('imdbID', models.CharField(blank=True, max_length=200)),
                ('Type', models.CharField(blank=True, max_length=200)),
                ('DVD', models.CharField(blank=True, max_length=200)),
                ('BoxOffice', models.CharField(blank=True, max_length=200)),
                ('Production', models.CharField(blank=True, max_length=200)),
                ('Website', models.CharField(blank=True, max_length=200)),
                ('Response', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
