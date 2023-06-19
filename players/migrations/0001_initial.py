# Generated by Django 2.1.15 on 2020-11-18 12:33

import core.backends.azure_storage
from django.db import migrations, models
import django.db.models.deletion
import players.utils.player


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'League',
                'verbose_name_plural': 'Leagues',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('position', models.CharField(choices=[('goalkeeper', 'GOALKEEPER'), ('side defender', 'SIDE DEFENDER'), ('central defender', 'CENTRAL DEFENDER'), ('defensive help', 'DEFENSIVE HELP'), ('middle help 8', 'MIDDLE HELP 8'), ('middle help 10', 'MIDDLE HELP 10'), ('side help 10', 'SIDE HELP'), ('attacker', 'ATTACKER')], max_length=16)),
                ('birth_date', models.DateField()),
                ('country', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('dominant_leg', models.CharField(choices=[('left', 'LEFT'), ('right', 'RIGHT'), ('none', 'NONE')], default='none', max_length=5)),
                ('is_active', models.BooleanField(default=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, storage=core.backends.azure_storage.AzureMediaStorage(), upload_to=players.utils.player.create_player_profile_picture_path)),
                ('status', models.CharField(choices=[('observation', 'OBSERVATION'), ('inappropriate', 'INAPPROPRIATE'), ('test', 'TEST')], default='observation', max_length=13)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='players.League')),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('country', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='players.Team'),
        ),
    ]
