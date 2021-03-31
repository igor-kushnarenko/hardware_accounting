from django.db import models


class Hardware(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='производитель',
        related_name='hardware'
    )
    type = models.ForeignKey(
        'Type',
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='тип',
        related_name='hardware'
    )
    model = models.CharField(max_length=50, verbose_name='модель')
    serial = models.CharField(max_length=50, verbose_name='серийный номер')
    place = models.ForeignKey(
        'Place',
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='расположение',
        related_name='hardware'
    )
    status = models.ForeignKey(
        'Status',
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        verbose_name='состояние',
        related_name='hardware'
    )
    comment = models.TextField(max_length=2000, verbose_name='Примечание', default='')

    def __str__(self):
        return f'{self.manufacturer} {self.model}'


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20, verbose_name='состояние')

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# TODO добавить модель ремонтов