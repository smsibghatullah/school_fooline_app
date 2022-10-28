from django.core.management.base import BaseCommand
from django.utils import timezone
from zk import ZK, const

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
        conn = None
        zk = ZK('192.168.1.100', port=4370, timeout=5)
        try:
            print('Connecting to device..........................')
            conn = zk.connect()
            print('Are you sure want to delete all data? [Y/N]: ')

            choices = input()
            if choices == 'Y':
                print ("Clear all data...")
                conn.clear_data()
            else:
                print ("Clear all data canceled !")
          
        except(Exception):
            print("Process terminate : ")
        finally:
            if conn:
                conn.disconnect()