from django import forms
from django.utils.translation import gettext_lazy as _

from course.models import HolidayCourseContact

class HolidayCoursePaymentForm(forms.ModelForm):
	class Meta:
		model = HolidayCourseContact
		fields = (
			'first_name', 'last_name', 'student_keen', 'is_student', 
			'amount_paid', 
			)
		labels = {
		'first_name': _('First Name'),
		'last_name': _('Last Name'),
		'student_keen': _('Are you keen??'),
		'is_student': _('Is the participant a student?'),
		'amount_paid': _('Name your price (these are tough times, I want to help)'),
		}

		widgets = {
		'amount_paid': forms.NumberInput(attrs={'step': 0.5}),
		}

