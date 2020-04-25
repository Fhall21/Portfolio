from django.conf import settings
from django.urls import path, re_path

from django.views.generic import TemplateView

from django.conf.urls import include
from course.views import (
	CourseLandingPageView,
	CoursePaymentPageView,
	# TestPage,
	)
from django.contrib import admin
# from rest_framework.routers import DefaultRouter

app_name="course"




# router = DefaultRouter()
# router.register('holiday-coding-course//', views.MeetingViewSet)

urlpatterns = [
    path('', CourseLandingPageView.as_view(template_name='course/course_landing.html'), name="python_course"),
    path('<str:referee>', CourseLandingPageView.as_view(template_name='course/course_landing.html'), name="python_course"),
    path('payment/', CoursePaymentPageView.as_view(template_name='course/course_payment.html'), name="python_payment"),
    # path('test-page/', TestPage.as_view(template_name='course/test_page.html'), name="test_page"),
    # path('test/', TemplateView.as_view(template_name='bookings/test2.html'), name="test"),
    # path('api/', include(router.urls))
]
