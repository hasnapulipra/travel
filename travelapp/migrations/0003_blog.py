# Generated by Django 3.2.11 on 2022-03-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_place_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('heading', models.CharField(max_length=100)),
                ('desc1', models.TextField()),
                ('img1', models.ImageField(upload_to='picture1')),
            ],
        ),
    ]
