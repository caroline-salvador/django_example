# Generated by Django 2.2.7 on 2019-11-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191107_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadosclimaticos',
            name='hora_medicao',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
