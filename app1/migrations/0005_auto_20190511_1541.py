# Generated by Django 2.2.1 on 2019-05-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20190511_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='nome',
            field=models.CharField(max_length=150, verbose_name='Gastos de entrada'),
        ),
        migrations.AlterField(
            model_name='saida',
            name='nome',
            field=models.CharField(max_length=150, verbose_name='Gastos de saída'),
        ),
    ]
