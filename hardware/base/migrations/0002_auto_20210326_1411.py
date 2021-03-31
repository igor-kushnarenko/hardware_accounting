# Generated by Django 2.2 on 2021-03-26 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardware',
            name='comment',
            field=models.TextField(default=None, max_length=2000, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='manufacturer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='hardware', to='base.Manufacturer', verbose_name='производитель'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='place',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='hardware', to='base.Place', verbose_name='расположение'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='hardware', to='base.Status', verbose_name='состояние'),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='hardware', to='base.Type', verbose_name='тип'),
        ),
    ]