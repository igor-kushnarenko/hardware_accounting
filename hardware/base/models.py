from django.db import models
from django.core import validators


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
    serial = models.CharField(
        max_length=50, 
        verbose_name='серийный номер',
        validators=[validators.MinLengthValidator(4)],
        error_messages={'min_length': 'Серийный номер слишком короткий! Не менее 4х символов.'}
        )
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

    class Meta:
        ordering = ['type']
        verbose_name_plural = 'Оборудование'
        verbose_name = 'Оборудование'
        unique_together = ('model', 'serial')


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Типы оборудования'
        verbose_name = 'Тип оборудования'
        ordering = ['name']


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Производители'
        verbose_name = 'Производитель'
        ordering = ['name']


class Status(models.Model):
    name = models.CharField(max_length=20, verbose_name='состояние')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Статусы'
        verbose_name = 'Статус'
        ordering = ['name']


class Place(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Расположения'
        verbose_name = 'Расположение'
        ordering = ['name']


class Repair(models.Model):
    date_repair = models.DateField(verbose_name='Дата отправки', null=True)
    problem = models.TextField(max_length=1000,verbose_name='Неисправность')
    contractor = models.CharField(max_length=30, verbose_name='Исполнитель')
    end_date_repair = models.DateField(verbose_name='Дата возврата', null=True)
    result = models.TextField(max_length=1000, verbose_name='Результат ремонта')
    cost = models.IntegerField(verbose_name='Стоимость ремонта', null=True)
    status = models.BooleanField(verbose_name='Активный', default=True)
    hardware = models.ForeignKey(
        Hardware,
        on_delete=models.SET_DEFAULT,
        default=True,
        null=True,
        verbose_name='Оборудование',
        related_name='hardware',
    )

    class Meta:
        verbose_name_plural = 'Ремонты'
        verbose_name = 'Ремонт'
        get_latest_by = 'date_repair'
        ordering = ['date_repair']