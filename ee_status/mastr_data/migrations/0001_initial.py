# Generated by Django 3.2.13 on 2022-10-02 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipality_key', models.CharField(max_length=200)),
                ('municipality', models.CharField(max_length=200)),
                ('county', models.CharField(max_length=200)),
                ('state', models.CharField(blank=True, max_length=200)),
                ('pv_net_nominal_capacity', models.FloatField()),
                ('wind_net_nominal_capacity', models.FloatField()),
                ('biomass_net_nominal_capacity', models.FloatField()),
                ('hydro_net_nominal_capacity', models.FloatField()),
                ('total_net_nominal_capacity', models.FloatField()),
                ('population', models.IntegerField()),
                ('nnc_per_capita', models.FloatField()),
                ('nnc_per_capita_rank_within_germany', models.IntegerField()),
                ('nnc_per_capita_rank_within_state', models.IntegerField()),
                ('nnc_per_capita_rank_within_county', models.IntegerField()),
            ],
            options={
                'db_table': 'current_totals',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MonthlyTimeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=None)),
                ('municipality_key', models.CharField(max_length=200)),
                ('municipality', models.CharField(max_length=200)),
                ('county', models.CharField(max_length=200)),
                ('state', models.CharField(blank=True, max_length=200)),
                ('pv_net_nominal_capacity', models.FloatField()),
                ('wind_net_nominal_capacity', models.FloatField()),
                ('biomass_net_nominal_capacity', models.FloatField()),
                ('hydro_net_nominal_capacity', models.FloatField()),
            ],
            options={
                'db_table': 'monthly_timeline_table',
                'managed': False,
            },
        ),
    ]
