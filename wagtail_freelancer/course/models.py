from django.db import models

#third party
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator, MinValueValidator



# Create your models here.
class ParentBaseHolidayCourseInterestData(models.Model):
	referee = models.CharField(max_length=200, default='', null=True, blank=True)
	first_name = models.CharField(max_length=50, default='')
	last_name = models.CharField(max_length=50, default='')
	student_keen = models.BooleanField(default=True)
	is_student = models.BooleanField(default=True)
	family_members = models.IntegerField(default=0)
	email = models.EmailField(unique=False, null=True, max_length=250)
	paid = models.BooleanField(default=False)
	amount_paid = models.DecimalField(
		validators=[MinValueValidator(30.00)], default=80.00, max_digits=6, decimal_places=2,)

	class Meta:
		abstract = True

	def __str__(self):
		return '{}'.format(self.first_name)



class EasterHolidayCourseInterestData(models.Model):
	referee = models.CharField(max_length=200, default='', null=True, blank=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	student_keen = models.BooleanField(default=True)
	is_student = models.BooleanField(default=True)
	family_members = models.IntegerField(default=0)
	email = models.EmailField(unique=False, null=True, max_length=250)
	paid = models.BooleanField(default=False)
	amount_paid = models.DecimalField(
		validators=[MinValueValidator(30.00)], default=50.00, max_digits=6, decimal_places=2,)

	def __str__(self):
		return '{}'.format(self.first_name)

class JuneJulyHolidayCourseInterestData(ParentBaseHolidayCourseInterestData):
	pass 