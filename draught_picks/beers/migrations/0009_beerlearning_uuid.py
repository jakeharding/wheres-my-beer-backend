# Generated by Django 2.0.1 on 2018-03-14 01:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0008_beer_calories'),
    ]

    operations = [
        migrations.AddField(
            model_name='beerlearning',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
