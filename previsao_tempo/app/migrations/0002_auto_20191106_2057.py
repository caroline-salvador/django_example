# Generated by Django 2.2.7 on 2019-11-06 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadosclimaticos',
            name='nascer_sol',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='dadosclimaticos',
            name='por_sol',
            field=models.DateTimeField(default=None),
        ),
    ]