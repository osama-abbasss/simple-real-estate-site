# Generated by Django 3.0.2 on 2020-01-07 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20200107_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='floor_number',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='garages_number',
            field=models.TextField(),
        ),
    ]
