# Generated by Django 2.2.3 on 2020-03-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0002_auto_20200306_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='picture',
            field=models.URLField(default=''),
        ),
    ]
