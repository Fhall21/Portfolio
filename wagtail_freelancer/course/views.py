import stripe, re, requests


from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
# from django.contrib.auth.models import User

from course.models import HolidayCourseContact
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
			print('form is valid')
			new_form = form_info.save(commit=False)
			# plan = stripe.Plan.retrieve("stripe Plan")
			first_name = form_info.cleaned_data.get('first_name', None)
			last_name = form_info.cleaned_data.get('last_name', None)
			amount_paid = int(form_info.cleaned_data.get('amount_paid', '00')) *100
			student_keen = form_info.cleaned_data.get('student_keen', True)
			is_student = form_info.cleaned_data.get('is_student', True)


			# print (form_info)
			# print (amount_paid)
			# print (request.POST)
			stripe_token = request.POST.get('stripeToken', '')
			email  = request.POST.get('stripeEmail', '')
			# stripe_sk = settings.STRIPE_SECRET_KEY

			#if token or email not blank, then make the payment
			paid = False
			if not(stripe_token == '') and not(email == ''):


				customer = stripe.Customer.create(
					name=first_name,
					email=email,
					source=stripe_token,
					)
				charge = stripe.Charge.create(
					customer=customer.id,
					description="Felix Hall Beginner Python Course",
					amount=amount_paid,
					currency='aud')


				#sending comfirmation email
				zapier_hook = settings.ZAPIER_COURSE_HOOK
				query_data={
				'first_name': first_name,
				'last_name': last_name,
				'amount_paid': amount_paid,
				'email': email,
				# 'email': 'fhall21@eq.edu.au',
				}
				r = requests.post(zapier_hook, data=query_data)

				paid = charge['paid']
				args['success'] = paid

				new_form.paid = paid
				new_form.email = email
				new_form.save()
			else:
				args['error'] = paid

			

		print (args)
		return render(request, self.template_name, args)
