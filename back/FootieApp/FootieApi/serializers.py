from rest_framework import serializers
from .models import Student, Attendance, TrainingDay, Week, Package, Report, Parent

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('parent',
                  'report',
                  'package',
                  'members',
                  'name',
                  'lastname',
                  'level',
                  'numLessonsPaid',
                  'numLessonsLeft',
                  'packageStatus',
                  'currentTerm',
                  'nextTerm',
                  'paidStatus',
                  'category',
                  'campus'
                  )

class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attendance
        fields = ('student', 'trainingday', 'attendance')

class TrainingDaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrainingDay
        fields = ('date',)

class WeekSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Week
        fields = ('startDate', 'days')

class PackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ('name', 'numLessons', 'weeks')

class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('title',
                  'date',
                  'englishReport',
                  'valuesReport',
                  'emotionalReport',
                  'nextTermReport',
                  'footballSkillsReport')

class ParentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parent
        fields = ('name', 'lastname', 'phone', 'emal')