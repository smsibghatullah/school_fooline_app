from django.core.management.base import BaseCommand
from django.utils import timezone
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
        zk = ZK('192.168.1.100', port=4370, verbose=True, timeout=60, password=0, force_udp=False, ommit_ping=False, encoding='UTF-8')
        try:
            conn = zk.connect()
            conn.set_user(uid=4, name='John Doe', privilege=0, password='123456', group_id='1', user_id='4', card=400)
        except Exception as e:
           print ("Process terminate : {}".format(e))
        finally:
            if conn:
                conn.disconnect()