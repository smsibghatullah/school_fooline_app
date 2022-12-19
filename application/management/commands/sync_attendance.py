from django.core.management.base import BaseCommand
from django.utils import timezone
import xmlrpc.client
import json
from application.models import Voucher
from django.core import serializers
from datetime import datetime


class Command(BaseCommand):
    help = 'Fetch and insert vouchers in db'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        # Voucher.objects.all().delete()
        self.stdout.write("Command Started At %s" % time)
        # ==========================================update attendance in odoo Starts
        url = 'http://192.168.1.114:8070/'
        db = 'ALHAMDSCHOOL'
        username = 'admin'
        password = 'admin'
        common = xmlrpc.client.ServerProxy('{}xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}xmlrpc/2/object'.format(url))
      
      
        
        date = datetime.date(datetime.now())
        current_date = date.strftime("%Y-%m-%d")
        attendance_standard = models.execute_kw(db, uid, password, 'daily.attendance','search',[[['date', '=', current_date]]])
        # print(json.dumps(attendance_standard, sort_keys=True, indent=4))
        
        student_row = models.execute_kw(db, uid, password, 'daily.attendance.line','search',[[['standard_id', 'in', attendance_standard],['stud_id', '=', 9]]])

        # print(student_row)
        attendance_standard = models.execute_kw(db, uid, password, 'daily.attendance.line','write',[student_row, {'is_present':True, "is_absent":False}])

        # ==========================================update attendance in odoo Ends
        time = timezone.now().strftime('%X')
        self.stdout.write("Command Ended At %s" % time)

 
