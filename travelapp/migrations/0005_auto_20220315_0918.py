# Generated by Django 3.2.11 on 2022-03-15 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_rename_name_blog_name1'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='month',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.IntegerField(),
        ),
    ]
