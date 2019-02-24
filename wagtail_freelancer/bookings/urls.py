from django.conf import settings
from django.urls import path, re_path

from django.views.generic import TemplateView

from django.conf.urls import include
from bookings import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter

app_name="bookings"




router = DefaultRouter()
router.register('meeting/', views.MeetingViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='bookings/booking.html'), name="bookings"),
    path('test/', TemplateView.as_view(template_name='bookings/test2.html'), name="test"),
    path('api/', include(router.urls))
,]
