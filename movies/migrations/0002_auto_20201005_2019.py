# Generated by Django 3.1.2 on 2020-10-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Actors',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Awards',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Director',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Genre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Metascore',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Plot',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Poster',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Rated',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Ratings',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Released',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Response',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Runtime',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Writer',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Year',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdbID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdbRating',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdbVotes',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
