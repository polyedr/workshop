# Generated by Django 2.0.7 on 2018-07-20 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='showdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
