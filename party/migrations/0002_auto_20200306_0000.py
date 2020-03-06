# Generated by Django 2.2.3 on 2020-03-05 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='decision',
            field=models.CharField(choices=[('PENDING', 'P'), ('ACCEPTED', 'A'), ('REJECTED', 'R')], default='PENDING', max_length=10),
        ),
    ]