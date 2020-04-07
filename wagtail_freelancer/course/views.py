import stripe, re, requests


from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
# from django.contrib.auth.models import User

from course.models import HolidayCourseInterestData
from course.forms import HolidayCoursePaymentForm, HolidayRegisterationForm

class CourseLandingPageView(TemplateView):
	template_name = 'course/course_landing.html'

	def get(self, request, referee=''):
		print(referee)
		number_of_applicants = len(HolidayCourseInterestData.objects.all())
		spots_left_num = 40 - number_of_applicants
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
	def post(self, request, referee=''):

		number_of_applicants = len(HolidayCourseInterestData.objects.all())
		spots_left_num = 40 - number_of_applicants

		
		form = HolidayRegisterationForm()
		args = {'form': form,
				'spots_left_num': spots_left_num,

		}

		form_info = HolidayRegisterationForm(request.POST)
		if form_info.is_valid():
			editable_form = form_info.save(commit=False)
			editable_form.referee = referee
			editable_form.save()
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


class CoursePaymentPageView(TemplateView):
	template_name = 'course/course_payment.html'

	def get(self, request):
		number_of_applicants = len(HolidayCourseInterestData.objects.all())
		spots_left_num = 40 - number_of_applicants
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
		'spots_left_num': spots_left_num,
		}
		return render(request, self.template_name, args)
	def post(self, request):
		number_of_applicants = len(HolidayCourseInterestData.objects.all())
		spots_left_num = 40 - number_of_applicants
		stripe_pk = settings.STRIPE_PUBLISHABLE_KEY

		
		form = HolidayCoursePaymentForm()
		args = {'form': form,
				'stripe_public_key': stripe_pk,
				'spots_left_num': spots_left_num,

		}

		form_info = HolidayCoursePaymentForm(request.POST)
		#checking if form is valid
		if form_info.is_valid():
			
			print('form is valid')

			#get form info 

			# plan = stripe.Plan.retrieve("stripe Plan")
			first_name = form_info.cleaned_data.get('first_name', None)
			last_name = form_info.cleaned_data.get('last_name', None)
			amount_chosen = int(form_info.cleaned_data.get('amount_paid', '00')) *100

			family_members = int(form_info.cleaned_data.get('family_members', '0'))

			amount_paid = amount_chosen + (15*family_members)

			#let's check if this person is already in the databse
			person, created = HolidayCourseInterestData.objects.get_or_create(
				first_name=first_name,
				last_name=last_name,
				)



			# get other info from the stripe form
			stripe_token = request.POST.get('stripeToken', '')
			email  = request.POST.get('stripeEmail', '')

			# just adding a bit of data in case person did not exist
			if not(created):
				person.referee = referee


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
				print (query_data)
				# r = requests.post(zapier_hook, data=query_data)

				paid = charge['paid']
				args['success'] = paid

				person.paid = paid
				person.email = email
				person.amount_paid = amount_paid
				person.family_members = family_members
				new_form.save()
			else:
				person.email = email
				args['error'] = paid

			

		print (args)
		return render(request, self.template_name, args)
