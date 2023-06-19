# Generated by Django 2.1.15 on 2020-11-29 17:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ranking', to='players.Player')),
            ],
            options={
                'verbose_name': 'Ranking',
                'verbose_name_plural': 'Rankings',
            },
        ),
    ]