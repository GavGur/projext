# Generated by Django 5.2 on 2025-04-20 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='login',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(default='', max_length=200),
        ),
    ]
