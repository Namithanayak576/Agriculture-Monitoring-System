from django.contrib import admin
from .models import Student,Teacher,Subject,Grade,Event

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'sex', 'student_class', 'phone_number', 'address', 'section')
    list_filter = ('section',)

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Event)