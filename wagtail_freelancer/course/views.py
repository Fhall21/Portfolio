import stripe, re, requests


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
		# intent = stripe.PaymentIntent.create(
		# 	amount=12000,
		# 	currency='aud',
			# )
		# stripe.setPublishableKey(stripe_pk)
		stripe_pk = settings.STRIPE_PUBLISHABLE_KEY
		# print ('pk {}'.format(stripe_pk))

		args = {
		'form': form,
		'stripe_public_key': stripe_pk,
		}
		return render(request, self.template_name, args)
	def post(self, request):
		stripe.api_key = settings.STRIPE_SECRET_KEY
		
		form = HolidayCoursePaymentForm()
		args = {'form': form,
				'key': settings.STRIPE_PUBLISHABLE_KEY
		}

		form_info = HolidayCoursePaymentForm(request.POST)
		if form_info.is_valid():
			# plan = stripe.Plan.retrieve("stripe Plan")
			first_name = form_info.cleaned_data['first_name']
			last_name = form_info.cleaned_data['last_name']
			amount_paid = int(form_info.cleaned_data['amount_paid']) *100
			student_keen = form_info.cleaned_data['student_keen']
			is_student = form_info.cleaned_data['is_student']
			# print (form_info)
			# print (amount_paid)
			# print (request.POST)
			stripe_token = request.POST['stripeToken']
			email  = request.POST['stripeEmail']
			# stripe_sk = settings.STRIPE_SECRET_KEY

			customer = stripe.Customer.create(
				email=email,
				source=stripe_token,
				)
			charge = stripe.Charge.create(
				customer=customer.id,
				description="Felix Hall Beginner Python Course",
				amount=amount_paid,
				currency='aud')
			# print (request.POST['stripeToken'])

			# subscription = stripe.Subscription.create(
			# 	customer=customer.id,
			# 	items=[
			# 		{
			# 	    "plan": plan,
			# 	    },
			# 	  ],
			# 	)

			zapier_hook = settings.ZAPIER_COURSE_HOOK
			query_data={
			'first_name': first_name,
			'last_name': last_name,
			'amount_paid': amount_paid,
			# 'email': email,
			'email': 'fhall21@eq.edu.au',
			}
			
			# r = requests.post(zapier_hook, data=query_data)



			print ('DONE!')


		return render(request, self.template_name, args)
