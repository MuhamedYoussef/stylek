# Generated by Django 2.1.3 on 2018-12-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_auto_20181217_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='rating',
            field=models.IntegerField(default=3),
        ),
    ]