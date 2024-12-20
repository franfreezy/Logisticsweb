# Generated by Django 5.1.1 on 2024-11-18 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_rename_location_locations_rename_order_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('is_checkpoint', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='orders',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='origin',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='checkpoints',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(max_length=100, unique=True)),
                ('truck_plate', models.CharField(max_length=100)),
                ('checkpoints', models.ManyToManyField(blank=True, related_name='order_checkpoints', to='backend.location')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_destination', to='backend.location')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_origin', to='backend.location')),
            ],
        ),
        migrations.DeleteModel(
            name='Locations',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
