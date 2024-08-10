# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.utils import timezone

class BUSES(models.Model):
	LICENSE_PLATE=models.CharField(max_length=50, primary_key=True)  #123aaa123?
	ROUTE_NAME=models.ForeignKey("ROUTES", on_delete=models.CASCADE)  #AB123
	D_NO=models.ForeignKey("DRIVERS", on_delete=models.CASCADE)        #D9874354
	C_NO=models.ForeignKey("CONDUCTORS", on_delete=models.CASCADE)        #C7435995

	class Meta:
		verbose_name = "Bus"
		verbose_name_plural = "Buses"

	def __str__(self):
		return self.LICENSE_PLATE

class DRIVERS(models.Model):
	D_NO=models.CharField(max_length=50, primary_key=True)        #D9874354
	D_NAME=models.CharField(max_length=50)      #SAMPANGI
	AGE=models.IntegerField()     #37
	SEX=models.CharField(max_length=1)          #M=F
	JOIN_DATE=models.DateField()
	EXPERIENCE=models.IntegerField()

	class Meta:
		verbose_name = "Driver"
		verbose_name_plural = "Drivers"

	@property
	def calculate_experience(self):
		today = timezone.now().date()
		join_date = self.JOIN_DATE
		experience_years = today.year - join_date.year
		if today.month < join_date.month or (today.month == join_date.month and today.day < join_date.day):
			experience_years -= 1
		return experience_years

	# Example usage:
	# driver = DRIVERS.objects.get(D_NO='D9874354')
	# print(driver.calculate_experience)

	def __str__(self):
		return self.D_NO

class CONDUCTORS(models.Model):
	C_NO=models.CharField(max_length=50, primary_key=True)
	C_NAME=models.CharField(max_length=50)
	AGE=models.IntegerField()
	SEX=models.CharField(max_length=1)
	JOIN_DATE=models.DateField()
	EXPERIENCE=models.IntegerField()

	class Meta:
		verbose_name = "Conductor"
		verbose_name_plural = "Conductors"

	@property
	def calculate_experience(self):
		today = timezone.now().date()
		join_date = self.JOIN_DATE
		experience_years = today.year - join_date.year
		if today.month < join_date.month or (today.month == join_date.month and today.day < join_date.day):
			experience_years -= 1
		return experience_years

	def __str__(self):
		return self.C_NO

class ROUTES(models.Model):
	ROUTE_NAME=models.CharField(max_length=50, primary_key=True)
	SOURCE=models.CharField(max_length=70)
	DESTINATION=models.CharField(max_length=70)
	PICKUP_TIME=models.TimeField()

	class Meta:
		verbose_name = "Route"
		verbose_name_plural = "Routes"

	def __str__(self):
		return self.ROUTE_NAME

class PASSENGERS(models.Model):
	P_NO=models.CharField(max_length=50, primary_key=True)
	P_NAME=models.CharField(max_length=50)
	SEX=models.CharField(max_length=1)
	ROUTE_NAME=models.ForeignKey("ROUTES", related_name="passenger_route", on_delete=models.CASCADE)
	PICKUP_TIME=models.ForeignKey("ROUTES", related_name="passenger_pickup_time", on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Passenger"
		verbose_name_plural = "Passengers"

	def __str__(self):
		return self.P_NAME