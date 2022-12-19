from django.core.management.base import BaseCommand
from django.utils import timezone
from application.models import Attendance
from datetime import datetime
import xmlrpc.client

# -*- coding: utf-8 -*-
import os
import sys

CWD = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from zk import ZK, const
import zk
print (zk.__file__)

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
        conn = None
        zk = ZK('192.168.1.103', port=4370, verbose=True, timeout=60)
        try:
                conn = zk.connect()
                for attendance in conn.live_capture():
                    if attendance is None:
                        pass
                    else:
                        att = str(attendance)

                        if att.find('<Attendance>:') != -1:
                            att = att.replace('<Attendance>:', '')
                            x = att.split(" : ")
                            student_id = x[0]
                            attendance_date = x[1][0: 19:]
                            stduent_attendance = Attendance(student_id=student_id,attendance_date=attendance_date)
                            stduent_attendance.save()
                            print ("===> ", student_id, attendance_date)
                            # ==========================================update attendance in odoo Starts
                            url = 'http://192.168.1.114:8070/'
                            db = 'school_api'
                            username = 'admin'
                            password = 'admin'
                            common = xmlrpc.client.ServerProxy('{}xmlrpc/2/common'.format(url))
                            uid = common.authenticate(db, username, password, {})
                            models = xmlrpc.client.ServerProxy('{}xmlrpc/2/object'.format(url))
                        
                        
                            
                            date = datetime.date(datetime.now())
                            current_date = date.strftime("%Y-%m-%d")
                            attendance_standard = models.execute_kw(db, uid, password, 'daily.attendance','search',[[['date', '=', current_date]]])
                            # print(json.dumps(attendance_standard, sort_keys=True, indent=4))
                            
                            student_row = models.execute_kw(db, uid, password, 'daily.attendance.line','search',[[['standard_id', 'in', attendance_standard],['stud_id', '=', int(student_id)]]])

                            # print(student_row)
                            attendance_standard = models.execute_kw(db, uid, password, 'daily.attendance.line','write',[student_row, {'is_present':True, "is_absent":False}])

                            # ==========================================update attendance in odoo Ends
        except Exception as e:
            print ("Process terminate : {}".format(e))
        finally:
            if conn:
                conn.disconnect()