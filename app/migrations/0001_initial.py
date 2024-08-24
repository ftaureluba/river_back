# Generated by Django 5.0.7 on 2024-08-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BirthModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10)),
                ('place', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CardsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yellow', models.IntegerField()),
                ('yellowred', models.IntegerField()),
                ('red', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DribblesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempts', models.IntegerField(blank=True)),
                ('success', models.IntegerField(blank=True)),
                ('past', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DuelsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(blank=True)),
                ('won', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoulsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drawn', models.IntegerField(blank=True)),
                ('committed', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GamesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appearences', models.IntegerField()),
                ('lineups', models.IntegerField()),
                ('minutes', models.IntegerField()),
                ('number', models.IntegerField(blank=True)),
                ('position', models.CharField(max_length=50)),
                ('rating', models.CharField(blank=True, max_length=10)),
                ('captain', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='GoalsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('conceded', models.IntegerField(blank=True)),
                ('assists', models.IntegerField(blank=True)),
                ('saves', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='LeagueModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('logo', models.URLField()),
                ('flag', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PassesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(blank=True)),
                ('key', models.IntegerField(blank=True)),
                ('accuracy', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PenaltyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('won', models.IntegerField(blank=True)),
                ('commited', models.IntegerField(blank=True)),
                ('scored', models.IntegerField()),
                ('missed', models.IntegerField()),
                ('saved', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('nationality', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
                ('injured', models.BooleanField()),
                ('photo', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ShotsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(blank=True)),
                ('on', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatisticsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SubstitutesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subbed_in', models.IntegerField()),
                ('subbed_out', models.IntegerField()),
                ('bench', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TacklesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(blank=True)),
                ('blocks', models.IntegerField(blank=True)),
                ('interceptions', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('logo', models.URLField()),
            ],
        ),
    ]
