# Generated by Django 2.2.4 on 2020-01-23 00:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200123_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beerprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='beer_profiles', to=settings.AUTH_USER_MODEL),
        ),
    ]