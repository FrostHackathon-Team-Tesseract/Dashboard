# Generated by Django 3.2.2 on 2021-05-08 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='Qulaitfication',
            field=models.CharField(default='NULL', max_length=30),
            preserve_default=False,
        ),
    ]
