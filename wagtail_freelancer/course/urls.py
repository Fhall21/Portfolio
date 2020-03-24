from django.conf import settings
from django.urls import path, re_path

from django.views.generic import TemplateView

from django.conf.urls import include
from course.views import (
	CourseLandingPageView,
	)
from django.contrib import admin
# from rest_framework.routers import DefaultRouter

app_name="bookings"




# router = DefaultRouter()
# router.register('holiday-coding-course//', views.MeetingViewSet)

urlpatterns = [
    path('', CourseLandingPageView.as_view(template_name='course/course.html'), name="course"),
    # path('test/', TemplateView.as_view(template_name='bookings/test2.html'), name="test"),
    # path('api/', include(router.urls))
]
