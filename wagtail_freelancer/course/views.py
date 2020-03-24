
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect, get_object_or_404

# from home.form import StripeForm, BTroopSignup, PTroopSignup, PricingFormA, PricingFormB
from django.conf import settings
# from django.contrib.auth.models import User

# from home.models import ContactForm, Payments
# from accounts.models import UserProfile, GroupRecord
from course.models import HolidayCourseContacts
from course.forms import HolidayCoursePaymentForm
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
# from freelancer import settings
# import stripe, bs4, time

class CourseLandingPageView(TemplateView):
	template_name = 'course/course.html'

	def get(self, request):
		form = HolidayCoursePaymentForm()
		args = {
		'form': form
		}
		return render(request, self.template_name, args)
	def post(self, request):
		stripe.api_key = freelancer.settings.base.STRIPE_TEST_SECRET_KEY
		
		form = HolidayCoursePaymentForm()

		print ('posted')
		args = {'form': form}

		form_info = HolidayCoursePaymentForm(request.post)
		if form_info.is_valid():
			print ('valid form')


		return render(request, self.template_name, args)
