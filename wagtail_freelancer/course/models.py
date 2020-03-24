from django.db import models

#third party
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator, MinValueValidator



# Create your models here.

class HolidayCourseContacts(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	student_keen = models.BooleanField(default=True)
	is_student = models.BooleanField(default=True)
	# phone_regex = RegexValidator(
	# 	regex=r'^\+?1?\d{9,15}$', 
	# 	message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
	# 	)

	# phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
	email = models.EmailField(unique=False, null=True, max_length=250)

	paid = models.BooleanField()
	amount_paid = models.DecimalField(
		validators=[MinValueValidator(10.00)], default=80.00, max_digits=6, decimal_places=2,)