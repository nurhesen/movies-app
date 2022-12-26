# Generated by Django 4.1.4 on 2022-12-25 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='DirectorsGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=300)),
                ('prob', models.FloatField()),
                ('director_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='directors.director')),
            ],
        ),
    ]