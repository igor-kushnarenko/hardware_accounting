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


class Repair(models.Model):
    date_repair = models.DateField(verbose_name='Дата отправки', null=True)
    problem = models.TextField(max_length=1000,verbose_name='Неисправность')
    contractor = models.CharField(max_length=30, verbose_name='Исполнитель')
    end_date_repair = models.DateField(verbose_name='Дата возврата', null=True)
    result = models.TextField(max_length=1000, verbose_name='Результат ремонта')
    cost = models.IntegerField(verbose_name='Стоимость ремонта', null=True)
    status = models.BooleanField(verbose_name='Активный', default=True)
    hardware = models.ForeignKey(
        'Hardware',
        on_delete=models.SET_DEFAULT,
        default=True,
        null=True,
        verbose_name='Оборудование',
        related_name='hardware',
    )