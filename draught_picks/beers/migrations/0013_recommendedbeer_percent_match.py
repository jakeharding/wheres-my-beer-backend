# Generated by Django 2.0.1 on 2018-04-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0012_recommendedbeer'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendedbeer',
            name='percent_match',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
