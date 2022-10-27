from django.db import models

class Student(models.Model):
    StudentId = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    AcademicYear = models.CharField(max_length=200)
    AcademicClass = models.CharField(max_length=200)
    School = models.CharField(max_length=200)
    AdmissionDate = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200)
    Status = models.CharField(max_length=200)

class Attendance(models.Model):
    StudentId = models.CharField(max_length=200)
    AttendanceDate = models.CharField(max_length=200)
    SmsStatus = models.CharField(max_length=200)

class Voucher(models.Model):
    StudentId = models.CharField(max_length=200)
    PostStatus = models.CharField(max_length=200)

class Fee(models.Model):
    StudentId = models.CharField(max_length=200)
    TotalFee = models.IntegerField()
    PaidAmount = models.IntegerField()
    DueAmount = models.IntegerField()
    FeeStructure = models.CharField(max_length=200)
    VoucherMonth = models.CharField(max_length=200)
    PostStatus = models.CharField(max_length=200)

class Admission(models.Model):
    StudentName = models.CharField(max_length=200)
    StudentClass = models.CharField(max_length=200)
    AdmissionFee = models.IntegerField()
    PaidAmount = models.IntegerField()
    BalanceAmount = models.IntegerField()
    DocRefCode = models.CharField(max_length=200)
    Status = models.CharField(max_length=200)



