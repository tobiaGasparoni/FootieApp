from django.db import models

class Admin(models.Model):
    accessCode = models.IntegerField()
    def __str__(self):
        return "%s" % (self.accessCode)

class Student(models.Model):

    PACKAGE_STATUS = (
        ('Activo', 'Activo'),
        ('Pendiente', 'Pendiente'),
    )

    LEVELS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )

    TERMS = (
        ('Primero', 'Primero'),
        ('Segundo', 'Segundo'),
        ('Tercero', 'Tercero'),
        ('Cuarto', 'Cuarto'),
    )

    PAID_STATUS = (
        ('Pagado', 'Pagado'),
        ('NoPagado', 'No Pagado'),
        ('PagadoEpayCo', 'Pagado con EpayCo')
    )

    CATEGORY = (
        ('Footie', 'Footie'),
        ('FootiePlay', 'Footie Play'),
    )

    parent = models.ForeignKey('Parent', on_delete=models.CASCADE, default="")
    report = models.ForeignKey('Report', on_delete=models.CASCADE, default="", null=True, blank = True)
    package = models.ForeignKey('Package', on_delete=models.CASCADE, default="", null=True, blank = True)
    members = models.ManyToManyField('TrainingDay', through='Attendance')
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    level = models.IntegerField(choices=LEVELS, default="")
    numLessonsPaid = models.IntegerField()
    numLessonsLeft = models.IntegerField()
    packageStatus = models.CharField(max_length=20, choices=PACKAGE_STATUS, default="")
    currentTerm = models.CharField(max_length=20, choices=TERMS, default="")
    nextTerm = models.CharField(max_length=20, choices=TERMS, default="")
    paidStatus = models.CharField(max_length=20, choices=PAID_STATUS, default="")
    category = models.CharField(max_length=20, choices=CATEGORY, default="")
    campus = models.CharField(max_length=20)

    def __str__(self):
        return "%s %s - %s, Remaining lessons: %s" % (self.name.upper(), self.lastname.upper(), self.campus, self.numLessonsLeft)

class Attendance(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    trainingday = models.ForeignKey('TrainingDay', on_delete=models.CASCADE)
    attendance = models.BooleanField

    def __str__(self):
        return "%s %s %r" % (self.student.name, self.trainingday, self.attendance)



class TrainingDay(models.Model):
    date = models.DateField()

    def __str__(self):
        return "%s" % (str(self.date))


class Week(models.Model):
    startDate = models.DateField()
    days = models.ManyToManyField(TrainingDay)

    def __str__(self):
        return "%s" % (str(self.startDate))


class Package(models.Model):
    name = models.CharField(max_length=100)
    numLessons = models.IntegerField()
    weeks = models.ManyToManyField(Week)

    def __str__(self):
        return "%s - Lessons: %s" % (self.name.upper(), self.numLessons)

class Report(models.Model):
    title = models.CharField(max_length=400, default="")
    date = models.DateField()
    englishReport = models.CharField(max_length=400)
    valuesReport = models.CharField(max_length=400)
    emotionalReport = models.CharField(max_length=400)
    nextTermReport = models.CharField(max_length=400)
    footballSkillsReport = models.CharField(max_length=400)

    def __str__(self):
        return "%s %s" % (self.title.upper(), str(self.date))



class Parent(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.IntegerField()
    emal = models.EmailField()

    def __str__(self):
        return "%s %s %s %s" % (self.name.upper(), self.lastname.upper(), self.emal, self.phone)