from django.contrib import admin

from .models import Student, Parent, Package, TrainingDay, Admin, Report

admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Package)
admin.site.register(TrainingDay)
admin.site.register(Admin)
admin.site.register(Report)
