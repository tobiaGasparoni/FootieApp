from rest_framework import serializers
from .models import Student, TrainingDay, Package, Report, Parent, Admin

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('parent',
                  'report',
                  'name',
                  'lastName',
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

class TrainingDaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrainingDay
        fields = ('date', 'student', 'attended')

class PackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ('name', 'numLessons', 'student')

class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('title',
                  'date',
                  'englishReport',
                  'valuesReport',
                  'emotionalReport',
                  'actionPoints',
                  'footballSkillsReport')

class ParentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parent
        fields = ('name', 'lastName', 'phone', 'email')

class AdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Admin
        fields = ('accessCode',)