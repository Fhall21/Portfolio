import stripe


from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
# from django.contrib.auth.models import User

from course.models import HolidayCourseContacts
from course.forms import HolidayCoursePaymentForm

class CourseLandingPageView(TemplateView):
	template_name = 'course/course.html'

	def get(self, request):
		form = HolidayCoursePaymentForm()
		args = {
		'form': form
		}
		return render(request, self.template_name, args)
	def post(self, request):
		stripe.api_key = settings.STRIPE_SECRET_KEY
		
		form = HolidayCoursePaymentForm()

		print ('posted')
		args = {'form': form}

		form_info = HolidayCoursePaymentForm(request.POST)
		if form_info.is_valid():
			print ('valid form')


		return render(request, self.template_name, args)
