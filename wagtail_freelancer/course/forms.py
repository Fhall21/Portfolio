from django import forms
from django.utils.translation import gettext_lazy as _

from course.models import HolidayCourseContacts

class HolidayCoursePaymentForm(forms.ModelForm):
	class Meta:
		model = HolidayCourseContacts
		fields = (
			'first_name', 'last_name', 'student_keen', 'is_student', 
			'amount_paid', 
			)
		labels = {
		'first_name': _('First Name'),
		'last_name': _('Last Name'),
		'student_keen': _('Are you keen??'),
		'is_student': _('Is the participant a student?'),
		'amount_paid': _('Name your price (free goodies for above $100)'),
		}

		widgets = {
		'amount_paid': forms.NumberInput(attrs={'step': 0.5}),
		}

