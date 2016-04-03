from django.db import models

class Area(models.Model):
    cityid = models.IntegerField(db_column='cityId')  # Field name made lowercase.
    provinceid = models.IntegerField(db_column='provinceId')  # Field name made lowercase.
    name = models.CharField(max_length=20)
    alias = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_area'


class City(models.Model):
    provinceid = models.IntegerField(db_column='provinceId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=20)
    alias = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tb_city'


class Province(models.Model):
    name = models.CharField(max_length=6)
    alias = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tb_province'