# Generated by Django 2.2 on 2021-03-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210326_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardware',
            name='comment',
            field=models.TextField(default='', max_length=2000, verbose_name='Примечание'),
        ),
    ]
