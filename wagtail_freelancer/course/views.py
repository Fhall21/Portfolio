import stripe, re, requests


from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
# from django.contrib.auth.models import User

from course.models import JuneJulyHolidayCourseInterestData
from course.forms import JuneJulyHolidayCoursePaymentForm, JuneJulyHolidayRegisterationForm

# class TestPage(TemplateView):
# 	template_name = 'course/test_page.html'
# 	def get(self, request):
# 		return render(request, self.template_name)

# 	def post(self, request):
# 		return render(request, self.template_name)


class CourseLandingPageView(TemplateView):
	template_name = 'course/course_landing.html'

	def get(self, request, referee=''):
		print(referee)
		if referee:
			request.session['referee'] = referee

		number_of_applicants = len(JuneJulyHolidayCourseInterestData.objects.all())
		spots_left_num = 10 - number_of_applicants
		form = JuneJulyHolidayRegisterationForm()
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
		'course_not_closed': False, # change when you want to reopen course

		}
		return render(request, self.template_name, args)
		
	def post(self, request, referee=''):

		number_of_applicants = len(JuneJulyHolidayCourseInterestData.objects.all())
		spots_left_num = 10 - number_of_applicants

		
		form = JuneJulyHolidayRegisterationForm()
		args = {'form': form,
				'course_not_closed': False, # change when you want to reopen course
				'spots_left_num': spots_left_num,

		}
		# return redirect('course:python_payment')


		form_info = JuneJulyHolidayRegisterationForm(request.POST)
		if form_info.is_valid():
			editable_form = form_info.save(commit=False)
			editable_form.referee = request.session.get('referee', '')
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
		number_of_applicants = len(JuneJulyHolidayCourseInterestData.objects.all())
		spots_left_num = 20 - number_of_applicants
		form = JuneJulyHolidayCoursePaymentForm()
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
		'course_not_closed': False, # change when you want to reopen course

		}
		return render(request, self.template_name, args)
	def post(self, request):
		print ('referee: ' + str(request.session.get('referee', '')))
		number_of_applicants = len(JuneJulyHolidayCourseInterestData.objects.all())
		spots_left_num = 20 - number_of_applicants
		stripe_pk = settings.STRIPE_PUBLISHABLE_KEY

		
		form = JuneJulyHolidayCoursePaymentForm()
		args = {'form': form,
				'stripe_public_key': stripe_pk,
				'spots_left_num': spots_left_num,
				'course_not_closed': False, # change when you want to reopen course
				

		}

		form_info = JuneJulyHolidayCoursePaymentForm(request.POST)
		#checking if form is valid
		if form_info.is_valid():
			
			print('form is valid')

			#get form info 

			# plan = stripe.Plan.retrieve("stripe Plan")
			first_name = form_info.cleaned_data.get('first_name', None)
			last_name = form_info.cleaned_data.get('last_name', None)
			amount_chosen = int(form_info.cleaned_data.get('amount_paid', '00')) *100

			family_members = int(form_info.cleaned_data.get('family_members', '0'))
			extra_names_list = []
			for extra_name_num in range(1,family_members+1):
				retreval_tag_last_name = 'last_name_{}'.format(extra_name_num)
				new_last_name = request.POST.get(retreval_tag_last_name, '')
				retreval_tag_first_name = 'first_name_{}'.format(extra_name_num)
				new_first_name = request.POST.get(retreval_tag_first_name, '')
				print (new_first_name)
				extra_names_list.append([new_first_name, new_last_name])

			print (extra_names_list)
			print(request.POST)

			amount_paid = amount_chosen + (1500*family_members)

			#let's check if this person is already in the databse
			person, created = JuneJulyHolidayCourseInterestData.objects.get_or_create(
				first_name=first_name,
				last_name=last_name,
				)



			# get other info from the stripe form
			stripe_token = request.POST.get('stripeToken', '')
			email  = request.POST.get('stripeEmail', '')



			# just adding a bit of data in case person did not exist
			if created:
				person.referee = request.session.get('referee', '')
				person.save()


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
				#two APIs?
				zapier_hook = settings.ZAPIER_COURSE_PAYMENT_HOOK
				family_confirmation = 'no other family members were added in the form.'
				if extra_names_list:
					family_confirmation = ''
					for name in extra_names_list:
						family_confirmation += "{}, ".format(name[0])
					if len(name) == 1:
						family_confirmation += 'is '
					else:
						family_confirmation += 'are '
					family_confirmation += 'also joining in within the course! Woo whoo!'
				query_data={
				'first_name': first_name,
				'family_confirmation': family_confirmation,
				'last_name': last_name,
				'amount_paid': (amount_paid/100),
				'email': email,
				# 'email': 'fhall21@eq.edu.au',
				}
				print (query_data)
				r = requests.post(zapier_hook, data=query_data)

				paid = charge['paid']
				args['success'] = paid

				person.paid = paid
				person.email = email
				person.amount_paid = (amount_paid/100)
				person.family_members = family_members
				person.save()

				# now for all the othere
				for name in extra_names_list:
					obj, created = JuneJulyHolidayCourseInterestData.objects.get_or_create(
					first_name=name[0],
					last_name=name[1],
					)
					obj.paid = paid
					obj.email = email
					obj.amount_paid = (amount_paid/100)
					obj.family_members = family_members					
					obj.save()

					#send a zapier email too!
				# new_form.save()
			else:
				person.email = email
				person.save()
				for name in extra_names_list:
					obj, created = JuneJulyHolidayCourseInterestData.objects.get_or_create(
					first_name=name[0],
					last_name=name[1],
					)
					if created:
						obj.email = email
					obj.save()


				args['error'] = paid

			

		print (args)
		return render(request, self.template_name, args)
