# Generated by Django 2.0.1 on 2018-03-12 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0004_auto_20180311_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='ibu',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
    ]
