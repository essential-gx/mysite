from django.db import models
from django.utils import timezone


# Create your models here.

class UserInfo(models.Model):
	"""员工表"""
	name = models.CharField(verbose_name="姓名", max_length=32)
	password = models.CharField(verbose_name="密码", max_length=64)
	age = models.IntegerField(verbose_name="年龄", default=2)
	account = models.DecimalField(verbose_name="余额", max_digits=10, decimal_places=2, default=0)
	create_time = models.DateTimeField(verbose_name="入职时间",default=timezone.now)
	depart = models.ForeignKey(to="Department",on_delete=models.CASCADE,to_field="id",null=True,blank=True)
	gender_choices=(
		(1,"男"),
		(2,"女")
	)
	gender = models.SmallIntegerField(verbose_name="性别",choices=gender_choices,default=None)
	
class Department(models.Model):
	"""部门表"""
	title = models.CharField(max_length=16)
