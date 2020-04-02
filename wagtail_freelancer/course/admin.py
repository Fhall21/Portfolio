from django.contrib import admin
from course.models import HolidayCourseInterestData

class HolidayCourseInterestAdmin(admin.ModelAdmin):
	model = HolidayCourseInterestData
	list_display = (
		'first_name', 'last_name', 'email', 'is_student', 'referee',
		)

admin.site.register(HolidayCourseInterestData, HolidayCourseInterestAdmin)
# Register your models here.
