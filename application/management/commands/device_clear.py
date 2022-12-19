from django.core.management.base import BaseCommand
from django.utils import timezone
from zk import ZK, const

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
        conn = None
        zk = ZK('192.168.1.103', port=4370, timeout=5)
        try:
            print('Connecting to device..........................')
            conn = zk.connect()
            conn.disable_device()
            
            users = conn.get_users()
            for user in users:
                conn.delete_user(uid=user.uid)
          
            conn.enable_device()          
        except(Exception):
            print("Process terminate : ")
            conn.enable_device()
        finally:
            if conn:
                conn.disconnect()