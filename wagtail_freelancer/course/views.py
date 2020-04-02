import stripe, re, requests


from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
# from django.contrib.auth.models import User

from course.models import HolidayCourseInterest
from course.forms import HolidayCoursePaymentForm, HolidayRegisterationForm

class CourseLandingPageView(TemplateView):
	template_name = 'course/course.html'

	def get(self, request):
		number_of_applicants = len(HolidayCourseInterest.objects.all())
		spots_left_num = 100 - number_of_applicants
		form = HolidayRegisterationForm()
		# intent = stripe.PaymentIntent.create(
		# 	amount=12000,
		# 	currency='aud',
			# )
		# stripe.setPublishableKey(stripe_pk)
		# stripe_pk = settings.STRIPE_PUBLISHABLE_KEY
		# print ('pk {}'.format(stripe_pk))

		args = {
		'form': form,
		'spots_left_num': spots_left_num,
		}
		return render(request, self.template_name, args)
	def post(self, request):
		number_of_applicants = len(HolidayCourseInterest.objects.all())
		spots_left_num = 100 - number_of_applicants

		
		form = HolidayRegisterationForm()
		args = {'form': form,
				'key': settings.STRIPE_PUBLISHABLE_KEY,
				'spots_left_num': spots_left_num,

		}

		form_info = HolidayRegisterationForm(request.POST)
		if form_info.is_valid():
			form_info.save()
			first_name = form_info.cleaned_data.get('first_name', None)
			last_name = form_info.cleaned_data.get('last_name', None)
			email = form_info.cleaned_data.get('email', None)

			if email and first_name and last_name:
				#sending comfirmation email
				zapier_hook = settings.ZAPIER_COURSE_HOOK
				query_data={
				'first_name': first_name,
				'last_name': last_name,
				'email': email,
				# 'email': 'fhall21@eq.edu.au',
				}
				r = requests.post(zapier_hook, data=query_data)
			
				args['success'] = True
			else:
				args['error'] = True

			

		print (args)
		return render(request, self.template_name, args)


class CoursePaymentLandingPageView(TemplateView):
	template_name = 'course/course_stripe.html'

	def get(self, request):
		number_of_applicants = len(HolidayCourseInterest.objects.all())
		spots_left_num = 100 - number_of_applicants
		form = HolidayCoursePaymentForm()
		# intent = stripe.PaymentIntent.create(
		# 	amount=12000,
		# 	currency='aud',
			# )
		# stripe.setPublishableKey(stripe_pk)
		# stripe_pk = settings.STRIPE_PUBLISHABLE_KEY
		# print ('pk {}'.format(stripe_pk))

		args = {
		'form': form,
		'stripe_public_key': stripe_pk,
		'spots_left_num': spots_left_num,
		}
		return render(request, self.template_name, args)
	def post(self, request):
		number_of_applicants = len(HolidayCourseInterest.objects.all())
		spots_left_num = 100 - number_of_applicants

		
		form = HolidayCoursePaymentForm()
		args = {'form': form,
				'key': settings.STRIPE_PUBLISHABLE_KEY,
				'spots_left_num': spots_left_num,

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

				stripe.api_key = settings.STRIPE_SECRET_KEY

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
				# will need a new API!
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
