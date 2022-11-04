from django.core.management.base import BaseCommand
from django.utils import timezone
from application.models import Attendance
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
        zk = ZK('192.168.1.108', port=4370, verbose=True, timeout=60)
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
        except Exception as e:
            print ("Process terminate : {}".format(e))
        finally:
            if conn:
                conn.disconnect()