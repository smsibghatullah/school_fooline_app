from django.core.management.base import BaseCommand
from django.utils import timezone
import xmlrpc.client
import json
from application.models import Voucher
from django.core import serializers

class Command(BaseCommand):
    help = 'Fetch and insert vouchers in db'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("Command Started At %s" % time)
        # ==========================================
        url = 'http://192.168.1.103:8070/'
        db = 'school_demo'
        username = 'admin'
        password = 'admin'
        common = xmlrpc.client.ServerProxy('{}xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}xmlrpc/2/object'.format(url))
        fee_vouchers = models.execute_kw(db, uid, password,
                  'student.payslip', 'search_read',
                  [[['id', '!=', 0], ['state', '=', 'confirm']]])
        if len(fee_vouchers) != 0:
            Voucher.objects.filter(received_amount=None).delete()
        # print(json.dumps(fee_vouchers[0], sort_keys=True, indent=4))
        for item in fee_vouchers:
            
            voucher = Voucher()
            voucher.voucher_id = item['id']
            voucher.paid_amount = item['paid_amount']
            voucher.due_amount = item['due_amount']
            voucher.total = item['total']
            voucher.student_id = item['student_id'][0]
            voucher.student_name = item['student_id'][1]
            voucher.display_name = item['display_name']
            voucher.company_id = item['company_id'][0]
            voucher.company_name = item['company_id'][1]
            voucher.voucher_date = item['date']
            voucher.division_id = item['division_id'][0]
            voucher.division_name = item['division_id'][1]
            voucher.voucher_status = item['state']
            voucher.save()
        
        
        # ==========================================
        time = timezone.now().strftime('%X')
        self.stdout.write("Command Ended At %s" % time)