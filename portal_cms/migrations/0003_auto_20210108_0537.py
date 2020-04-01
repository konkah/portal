# Generated by Django 2.2.17 on 2021-01-08 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_cms', '0002_auto_20210108_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poseidon',
            name='count',
            field=models.IntegerField(null=True, verbose_name='Quantidade que será mostrada'),
        ),
        migrations.AlterField(
            model_name='poseidon',
            name='max_characters',
            field=models.IntegerField(null=True, verbose_name='Máximo de caracteres do texto'),
        ),
    ]
