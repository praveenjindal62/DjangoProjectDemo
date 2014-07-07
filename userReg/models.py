from django.db import models
from django.forms import ModelForm


GENDER_CHOICES=(('M','Male'),('F','Female'))
class UserDetails(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	uname=models.CharField(max_length=100)
	email=models.EmailField();
	
	gender=models.CharField(max_length=1,choices=GENDER_CHOICES)


class UserDetailsForm(ModelForm):
	class Meta:
		model=UserDetails
		fields=['fname','lname','uname','email','gender']

# Create your models here.
