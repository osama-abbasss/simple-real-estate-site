# Generated by Django 3.0.2 on 2020-01-08 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0008_remove_governorate_the_property'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReserveProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
