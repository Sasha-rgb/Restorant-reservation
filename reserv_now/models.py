from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True


class HallOne(models.Model):
    table_name = models.CharField(max_length=50)
    table_picture = models.ImageField(upload_to="hall_one_tables")
    price = models.IntegerField()
    discription = models.CharField(max_length=1000)
    reserved = models.BooleanField()
    count_of_chair = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Hall'

    def __str__(self):
        return self.table_name


class HallTwo(models.Model):
    table_name = models.CharField(max_length=50)
    table_picture = models.ImageField(upload_to="hall_two_tables")
    price = models.IntegerField()
    discription = models.CharField(max_length=1000)
    reserved = models.BooleanField()
    count_of_chair = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Hall [2]'

    def __str__(self):
        return self.table_name


class VipHall(models.Model):
    table_name = models.CharField(max_length=50)
    table_picture = models.ImageField(upload_to="vip_hall_tables")
    price = models.IntegerField()
    discription = models.CharField(max_length=1000)
    reserved = models.BooleanField()
    count_of_chair = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Vip hall'

    def __str__(self):
        return self.table_name