# Generated by Django 3.0.2 on 2020-01-07 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_auto_20200107_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='governorate',
            name='the_property',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='governorate_property', to='properties.Property'),
            preserve_default=False,
        ),
    ]
