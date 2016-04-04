from django.db import models


class Area(models.Model):
    cityId = models.IntegerField(db_column='cityId')  # Field name made lowercase.
    provinceId = models.IntegerField(db_column='provinceId')  # Field name made lowercase.
    name = models.CharField(max_length=20)
    alias = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_area'


class City(models.Model):
    provinceId = models.IntegerField(db_column='provinceId', blank=True, null=True)  # Field name made lowercase.
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


class SmsRecord(models.Model):
    userId = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    phoneNo = models.CharField(db_column='phoneNo', max_length=11, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=256, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    gmtCreate = models.DateTimeField(db_column='gmtCreate', blank=True, null=True)  # Field name made lowercase.
    verifyCode = models.CharField(db_column='verifyCode', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_sms_record'


class SmsTemplate(models.Model):
    type = models.CharField(primary_key=True, max_length=12)
    templateContent = models.CharField(db_column='templateContent', max_length=256, blank=True, null=True)  # Field name made lowercase.
    gmtModified = models.DateTimeField(db_column='gmtModified')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_sms_template'


class SmsType(models.Model):
    type = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_sms_type'


class Config(models.Model):
    configName = models.CharField(db_column='configName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    configContent = models.CharField(db_column='configContent', max_length=256, blank=True, null=True)  # Field name made lowercase.
    gmtCreate = models.DateTimeField(db_column='gmtCreate', blank=True, null=True)  # Field name made lowercase.
    gmtModified = models.DateTimeField(db_column='gmtModified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_config'

