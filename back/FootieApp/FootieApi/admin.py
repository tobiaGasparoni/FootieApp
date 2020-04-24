from django.contrib import admin

from .models import Student, Parent, Package, Week, TrainingDay, Admin, Report, Attendance

admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Package)
admin.site.register(Week)
admin.site.register(TrainingDay)
admin.site.register(Admin)
admin.site.register(Report)
admin.site.register(Attendance)
