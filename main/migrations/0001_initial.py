# Generated by Django 4.0.3 on 2022-03-03 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('rating', models.FloatField(blank=True)),
                ('runtime', models.FloatField()),
                ('year', models.DateField()),
                ('genre', models.CharField(choices=[('comedy', 'comedy'), ('action', 'action'), ('drama', 'drama')], max_length=25)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(blank=True)),
                ('actors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.actor')),
            ],
        ),
    ]
