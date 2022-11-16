from django.db import models


# Create your models here.

class NewPerson(models.Model):
    name = models.CharField(max_length=10, verbose_name='姓名')
    sex = models.CharField(max_length=2, verbose_name='性别')
    phone = models.CharField(max_length=15, verbose_name='手机号', primary_key=True)
    address = models.TextField(verbose_name='住址')
    activity = models.CharField(max_length=10, verbose_name='活动')
    department = models.CharField(max_length=10, verbose_name='部门')
    changeable = models.CharField(max_length=2, verbose_name='是否接受调剂')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '社区新人'
        verbose_name_plural = '社区新人名单'


class CommunityPerson(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=10, verbose_name='姓名')
    sex = models.CharField(max_length=2, verbose_name='性别')
    phone = models.CharField(max_length=15, verbose_name='手机号')
    address = models.TextField(verbose_name='住址')
    activity = models.TextField(verbose_name='活动')
    department = models.CharField(max_length=10, verbose_name='部门')
    department_job = models.CharField(max_length=10, verbose_name='部门职务')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '社区人员信息'
        verbose_name_plural = '社区人员信息表'
