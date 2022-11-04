from django.core.management.base import BaseCommand
from django.utils import timezone
from application.models import Student
import os
import sys
import time

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
        zk = ZK('192.168.1.108', port=4370, timeout=5)
        try:
            students = Student.objects.all()
            conn = zk.connect()
            for student in students:
                user = {int(student.student_id), student.display_name,0,123456,student.division_name,int(student.student_id), int(student.student_id)}
                print(user)
                conn.set_user(
                    uid=int(student.student_id), 
                    name=student.display_name, 
                    privilege=0, 
                    password='123456', 
                    group_id=str(student.division_name), 
                    user_id=str(student.student_id), 
                    card=str(student.student_id))

            # conn.set_user(uid=4, name='John Doe', privilege=0, password='123456', group_id='1', user_id='4', card='400')
        except Exception as e:
           print ("Process terminate : {}".format(e))
        finally:
            if conn:
                conn.disconnect()