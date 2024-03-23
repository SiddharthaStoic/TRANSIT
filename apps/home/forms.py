from django import forms
from .models import BUSES, DRIVERS, CONDUCTORS, ROUTES, PASSENGERS

class Driverform(forms.ModelForm):
	class Meta:
		model = DRIVERS
		fields = ['D_NAME', 'D_NO', 'AGE', 'SEX', 'JOIN_DATE', 'EXPERIENCE']

class Conductorform(forms.ModelForm):
	class Meta:
		model = CONDUCTORS
		fields = ['C_NAME', 'C_NO', 'AGE', 'SEX', 'JOIN_DATE', 'EXPERIENCE']