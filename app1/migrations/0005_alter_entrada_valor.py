# Generated by Django 3.2.4 on 2021-06-23 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20210623_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='valor',
            field=models.IntegerField(),
        ),
    ]
