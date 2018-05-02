# Generated by Django 2.0.1 on 2018-03-13 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0008_beer_calories'),
        ('users', '0005_auto_20180302_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='beerpreferences',
            name='beer_learning',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='beers.BeerLearning'),
        ),
        migrations.AddField(
            model_name='draughtpicksuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='F', max_length=1),
        ),
    ]
