# Generated by Django 3.0.2 on 2020-01-07 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20200107_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='city',
            field=models.CharField(default='nasr', max_length=400),
            preserve_default=False,
        ),
    ]
