from rest_framework import viewsets
from .serializers import StudentSerializer, AttendanceSerializer, TrainingDaySerializer, WeekSerializer, PackageSerializer, ReportSerializer, ParentSerializer
from .models import Student, Attendance, TrainingDay, Week, Package, Report, Parent

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class TrainingDayViewSet(viewsets.ModelViewSet):
    queryset = TrainingDay.objects.all()
    serializer_class = TrainingDaySerializer

class WeekViewSet(viewsets.ModelViewSet):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer