from django import forms
from django.utils.translation import gettext_lazy as _

from course.models import (
	EasterHolidayCourseInterestData, 
	JuneJulyHolidayCourseInterestData,
	)

family_members_choices= (('0','0'),('1','1'), ('2','2'), ('3','3'),)

HolidayCourseFormOptions= {
	'interest':{
		'fields': (
				'first_name', 'last_name', 'email', 'student_keen', 'is_student', 
				),
		'labels_interest': {
			'first_name': _('First name'),
			'last_name': _('Last name'),
			'email': _('Best email of contact'),
			'student_keen': _('Are you keen?'),
			'is_student': _('Is the participant a student?'),
			'amount_paid': _("Name your price (these are tough times, I want to help. Just don't pass the minimum!)"),
			},
		},

	'payment':{
		'fields': (
			'first_name', 'last_name', 'family_members', 
			'amount_paid', 
			),
		'labels': {
			'first_name': _('First name (that you registered with)'),
			'last_name': _('Last name (that you registered with)'),
			'family_members': _('How many ADDITIONAL family members would like to join?'),
			'amount_paid': _("Name your price (whatever you feel comfortable with). Just don't pass the minimum!)"),
			},
		'widgets': {
			'family_members': forms.Select(choices = family_members_choices),
			'amount_paid': forms.NumberInput(attrs={
				'step': 0.5,
				'data-content':'psst... minimum of $30.',
				'data-placement': 'top',
				'data-container': 'body',
				'data-toggle': 'popover',
			}),
		},
	}
}

class EasterHolidayRegisterationForm(forms.ModelForm):
	class Meta:
		model = EasterHolidayCourseInterestData
		fields = HolidayCourseFormOptions['interest']['fields']
		labels = HolidayCourseFormOptions['interest']


class JuneJulyHolidayRegisterationForm(forms.ModelForm):
	class Meta:
		model = JuneJulyHolidayCourseInterestData
		fields = HolidayCourseFormOptions['interest']['fields']
		labels = HolidayCourseFormOptions['interest']


class EasterHolidayCoursePaymentForm(forms.ModelForm):
	class Meta:
		model = EasterHolidayCourseInterestData
		fields = HolidayCourseFormOptions['payment']['fields']
		labels = HolidayCourseFormOptions['payment']['labels']
		widgets = HolidayCourseFormOptions['payment']['widgets']

class JuneJulyHolidayCoursePaymentForm(forms.ModelForm):
	class Meta:
		model = JuneJulyHolidayCourseInterestData
		fields = HolidayCourseFormOptions['payment']['fields']
		labels = HolidayCourseFormOptions['payment']['labels']
		widgets = HolidayCourseFormOptions['payment']['widgets']