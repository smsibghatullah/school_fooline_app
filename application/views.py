from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView # Import TemplateView
from .models import Voucher, Admission
from django.http import JsonResponse
from datetime import datetime
import json

def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        # 'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def charts(request):
    template = loader.get_template('charts.html')
    context = {
        # 'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def vouchers(request):
    vouchers_list = Voucher.objects.order_by('id')
    template = loader.get_template('vouchers.html')
    context = {
        'vouchers_list': vouchers_list,
    }
    return HttpResponse(template.render(context, request))

def postvoucher(request):
    voucher = Voucher.objects.filter(voucher_id=request.POST['voucher_id']).update(received_amount=request.POST['received_amount'], offline_status='received waiting for sync', received_date=datetime.date(datetime.now()))
    # voucher = Voucher.objects.get(id=1)
    return JsonResponse({'received_amount':request.POST['received_amount'], 'voucher_id': request.POST['voucher_id']})

def admission(request):
    list = Admission.objects.order_by('id')
    if request.method == 'GET':
         template = loader.get_template('admission.html')
         context = {'list': list}
         return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        #  data = Admission(request.POST)   
         data = Admission(student_name=request.POST['student_name'], student_class=request.POST['student_class'], admission_fee=request.POST['admission_fee'], paid_amount=request.POST['paid_amount'], balance_amount=request.POST['balance_amount'], document_referance=request.POST['document_referance'], status='Created')   
         data.save()
         reponse = {'status':False, 'message':'', 'data':{}}

         return JsonResponse(reponse, status=200)
    elif request.method == 'DELETE':
           id =  request.GET['id']
        
           reponse = {'status':False, 'message':'', 'data':id}
           data = Admission.objects.filter(id=id).delete()

           return JsonResponse({}, status=200)
