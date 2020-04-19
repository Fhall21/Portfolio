from django.contrib import admin
from course.models import (
	ParentBaseHolidayCourseInterestData,
	EasterHolidayCourseInterestData, 
	JuneJulyHolidayCourseInterestData,
	)

class BaseHolidayCourseInterestAdmin(admin.ModelAdmin):
	model = ParentBaseHolidayCourseInterestData
	list_display = (
		'first_name', 'last_name', 'email', 'is_student', 'referee',
	)

class EasterHolidayCourseInterestAdmin(admin.ModelAdmin):
	model = EasterHolidayCourseInterestData
	list_display = (
		'first_name', 'last_name', 'email', 'is_student', 'referee',
		)
admin.site.register(EasterHolidayCourseInterestData, EasterHolidayCourseInterestAdmin)


class JuneJulyHolidayCourseInterestDataAdmin(BaseHolidayCourseInterestAdmin):
	model = JuneJulyHolidayCourseInterestData

admin.site.register(JuneJulyHolidayCourseInterestData, JuneJulyHolidayCourseInterestDataAdmin)

# Register your models here.
