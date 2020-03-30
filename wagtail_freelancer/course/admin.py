from django.contrib import admin
from course.models import HolidayCourseInterest

class HolidayCourseInterestAdmin(admin.ModelAdmin):
	list_display = (
		'first_name', 'last_name', 'amount_paid', 'paid', 'email', 'is_student',
		)

admin.site.register(HolidayCourseInterest, HolidayCourseInterestAdmin)
# Register your models here.
