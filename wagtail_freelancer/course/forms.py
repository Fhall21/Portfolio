from django import forms
from django.utils.translation import gettext_lazy as _

from course.models import HolidayCourseInterestData

class HolidayRegisterationForm(forms.ModelForm):
	class Meta:
		model = HolidayCourseInterestData
		fields = (
			'first_name', 'last_name', 'email', 'student_keen', 'is_student', 
			)
		labels = {
		'first_name': _('First name'),
		'last_name': _('Last name'),
		'email': _('Best email of contact'),
		'student_keen': _('Are you keen?'),
		'is_student': _('Is the participant a student?'),
		'amount_paid': _("Name your price (these are tough times, I want to help. Just don't pass the minimum!)"),
		}


class HolidayCoursePaymentForm(forms.ModelForm):
	class Meta:
		model = HolidayCourseInterestData
		fields = (
			'first_name', 'last_name', 'family_members', 
			'amount_paid', 
			)
		labels = {
		'first_name': _('First name (that you registered with)'),
		'last_name': _('Last name (that you registered with)'),
		'family_members': _('How many ADDITIONAL family members would like to join?'),
		'amount_paid': _("Name your price (these are tough times, I want to help. Just don't pass the minimum!)"),
		}

		family_members_choices = (('0','0'),('1','1'), ('2','2'), ('3','3'), ('4','4'),)

		# choices = {
		# 'family_members': family_members_choices,
		# }
		widgets = {
		'family_members': forms.Select(choices = family_members_choices),
		'amount_paid': forms.NumberInput(attrs={
			'step': 0.5,
			'data-content':'psst... minimum of $30.',
			'data-placement': 'top',
			'data-container': 'body',
			'data-toggle': 'popover',
			}),
		}

