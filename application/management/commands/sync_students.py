from django.core.management.base import BaseCommand
from django.utils import timezone
import xmlrpc.client
import json
from application.models import Student
from django.core import serializers

class Command(BaseCommand):
    help = 'Fetch and insert vouchers in db'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("Command Started At %s" % time)
        # ==========================================
        url = 'http://192.168.1.101:8070/'
        db = 'school_demo'
        username = 'admin'
        password = 'admin'
        common = xmlrpc.client.ServerProxy('{}xmlrpc/2/common'.format(url))
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}xmlrpc/2/object'.format(url))
        school_student = models.execute_kw(db, uid, password, 'student.student', 'search_read',  [[['id', '!=', 0]]])
        if len(school_student) != 0:
            Student.objects.all().delete()
        # print(json.dumps(school_student[0], sort_keys=True, indent=4))
        for item in school_student:
            # print(json.dumps( item , sort_keys=True, indent=4))
            # break

            school_student = Student()
            school_student.student_id = item['id']
            school_student.display_name = item['display_name']
            school_student.Acadamic_year = item['Acadamic_year']
            school_student.standard_id = item['standard_id'][0] if len(item['standard_id']) > 0 else ''
            school_student.standard_name = item['standard_id'][1] if len(item['standard_id']) > 0 else ''
            school_student.partner_id = item['partner_id'][1] if len(item['partner_id']) > 0 else ''
            school_student.division_id = item['division_id'][0] if len(item['division_id']) > 0 else ''
            school_student.division_name = item['division_id'][1] if len(item['division_id']) > 0 else ''
            school_student.parent_name = item['parent_name']
            school_student.student_code = item['student_code']
            school_student.year_id = item['year'][0] if len(item['year']) > 0 else ''
            school_student.year_name = item['year'][1] if len(item['year']) > 0 else ''
            school_student.state = item['state']
            school_student.save()
        
        # data = serializers.serialize('json',Voucher.objects.all())
        # print(json.dumps(data, sort_keys=True, indent=4))    


        # ==========================================
        time = timezone.now().strftime('%X')
        self.stdout.write("Command Ended At %s" % time)