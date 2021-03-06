# Generated by Django 2.0.1 on 2018-03-18 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beers', '0010_beerlearning_melon'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLearningProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('scaled_ibu', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('scaled_abv', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('malt', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('hops', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('india', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('america', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('german', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('belgium', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('ireland', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('europe', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('bohemian', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('baltic', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('coffee', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('chocolate', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('caramel', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('wheat', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('vanilla', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('strawberry', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('almond', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('coconut', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('pineapple', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('plum', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('mango', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('orange', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('peach', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('toffee', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('melon', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('honey', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('hazelnut', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('blueberry', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('banana', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('pumpkin', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('tart', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('sour', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('sweet', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('dry', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('oats', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('light_colors', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('dark_colors', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('bitter', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('lambic', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('lager', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('porter', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('stouts', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('ales', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='learning_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='beerlearning',
            name='scaled_abv',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='beerlearning',
            name='scaled_ibu',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=4),
        ),
    ]
