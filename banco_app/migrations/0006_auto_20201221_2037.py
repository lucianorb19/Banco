# Generated by Django 3.1.4 on 2020-12-21 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco_app', '0005_auto_20201221_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nascimento',
            field=models.CharField(max_length=30),
        ),
    ]
