from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Meeting(models.Model):

	name = models.CharField(max_length=150, blank= True, null=True)
	phone_regex = RegexValidator(
		regex=r'^\+?1?\d{9,15}$', 
		message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
		)

	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
	email = models.EmailField(blank=True, unique=False, null=True, max_length=250)
	day_time = models.DateTimeField(blank=True, null=False, unique=True)
