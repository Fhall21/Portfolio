from django.contrib import admin
from course.models import HolidayCourseContact

class HolidayCourseContactAdmin(admin.ModelAdmin):
	list_display = (
		'first_name', 'last_name', 'amount_paid', 'paid', 'email', 'is_student',
		)

admin.site.register(HolidayCourseContact, HolidayCourseContactAdmin)
# Register your models here.
