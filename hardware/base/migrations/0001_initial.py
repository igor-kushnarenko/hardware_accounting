# Generated by Django 2.2 on 2021-03-26 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='состояние')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='модель')),
                ('serial', models.CharField(max_length=50, verbose_name='серийный номер')),
                ('comment', models.TextField(max_length=2000, verbose_name='Примечание')),
                ('manufacturer', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hardware', to='base.Manufacturer', verbose_name='производитель')),
                ('place', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hardware', to='base.Place', verbose_name='расположение')),
                ('status', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hardware', to='base.Status', verbose_name='состояние')),
                ('type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hardware', to='base.Type', verbose_name='тип')),
            ],
        ),
    ]
