# Generated by Django 2.2.3 on 2020-03-06 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0003_customer_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
    ]
