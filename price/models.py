from django.db import models
import django.utils.timezone as timezone
# Create your models here.


class Item(models.Model):    #创建工程列表
    iname = models.CharField(max_length=200, blank=True, null=True, verbose_name='工程名称')
    idate = models.DateTimeField(default=None, auto_now=False, auto_now_add=False, verbose_name='项目日期')
    inum = models.IntegerField(blank=True, null=True, verbose_name='数量')
    iprice = models.FloatField(blank=True, null=True, verbose_name='单价')
    isUrgency = models.BooleanField(default=False, verbose_name='是否加急') 
    toWhere = models.CharField(max_length=10, blank=True, null=True, verbose_name='运送方式')
    imemo = models.CharField(max_length=300, blank=True, null=True, verbose_name='项目备注')
    itaxi = models.IntegerField(default=13, blank=True, null=True, verbose_name='税率')
    tcount = models.FloatField(blank=True, null=True, verbose_name='含税费用')
    shipcount = models.FloatField(blank=True, null=True, verbose_name='运费')
    itotal = models.FloatField(blank=True, null=True, verbose_name='合计价格')
    add_date = models.DateTimeField(default=timezone.now, verbose_name='添加日期')
    mod_date = models.DateTimeField(auto_now = True, verbose_name='最后修改日期')
    pid = models.IntegerField(blank=True, null=True, verbose_name='项目ID')
    oid = models.IntegerField(blank=True, null=True, verbose_name='机构ID')
    

class Organization(models.Model):     #创建机构列表
    oname = models.CharField(max_length=200, blank=True, null=True, verbose_name='机构名称')


class Project(models.Model):      #创建项目列表
    pname = models.CharField(max_length=200, blank=True, null=True, verbose_name='项目名称')
    oid = models.IntegerField(blank=True, null=True, verbose_name='机构ID')
