# Generated by Django 3.0 on 2021-02-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210218_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='notes',
            field=models.CharField(max_length=200),
        ),
    ]