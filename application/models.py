from __future__ import division
from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=200, null=True, blank=True)
    display_name = models.CharField(max_length=200, null=True, blank=True)
    Acadamic_year = models.CharField(max_length=200, null=True, blank=True)
    standard_id = models.CharField(max_length=200, null=True, blank=True)
    standard_name = models.CharField(max_length=200, null=True, blank=True)
    partner_id = models.CharField(max_length=200, null=True, blank=True)
    division_id = models.CharField(max_length=200, null=True, blank=True)
    division_name = models.CharField(max_length=200, null=True, blank=True)
    parent_name = models.CharField(max_length=200, null=True, blank=True)
    student_code = models.CharField(max_length=200, null=True, blank=True)
    year_id = models.CharField(max_length=200, null=True, blank=True)
    year_name = models.CharField(max_length=200, null=True, blank=True)   
    state = models.CharField(max_length=200, null=True, blank=True)

class Attendance(models.Model):
    StudentId = models.CharField(max_length=200)
    AttendanceDate = models.CharField(max_length=200)
    SmsStatus = models.CharField(max_length=200)

class Voucher(models.Model):
   voucher_id = models.CharField(max_length=200, null=True, blank=True)
   paid_amount = models.IntegerField(null=True, blank=True)
   due_amount = models.IntegerField(null=True, blank=True)
   total = models.IntegerField(null=True, blank=True)
   student_id = models.CharField(max_length=200, null=True, blank=True)
   student_name = models.CharField(max_length=200, null=True, blank=True)
   display_name = models.CharField(max_length=200, null=True, blank=True)
   company_id = models.CharField(max_length=200, null=True, blank=True)
   company_name = models.CharField(max_length=200, null=True, blank=True)
   voucher_date = models.CharField(max_length=200, null=True, blank=True)
   division_id = models.CharField(max_length=200, null=True, blank=True)
   division_name = models.CharField(max_length=200, null=True, blank=True)
   voucher_status = models.CharField(max_length=200, null=True, blank=True)
   journal_id = models.CharField(max_length=200, null=True, blank=True)
   received_date = models.CharField(max_length=200, null=True, blank=True)
   received_amount = models.CharField(max_length=200, null=True, blank=True)
   offline_status = models.CharField(max_length=200, null=True, blank=True) # unposted, posted, error


class Fee(models.Model):
    StudentId = models.CharField(max_length=200)
    TotalFee = models.IntegerField()
    PaidAmount = models.IntegerField()
    DueAmount = models.IntegerField()
    FeeStructure = models.CharField(max_length=200)
    VoucherMonth = models.CharField(max_length=200)
    PostStatus = models.CharField(max_length=200)

class Admission(models.Model):
    student_name = models.CharField(max_length=200)
    student_class = models.CharField(max_length=200)
    admission_fee = models.IntegerField()
    paid_amount = models.IntegerField()
    balance_amount = models.IntegerField()
    document_referance = models.CharField(max_length=200)
    status = models.CharField(max_length=200)



