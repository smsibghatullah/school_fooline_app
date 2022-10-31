from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView # Import TemplateView


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
    template = loader.get_template('vouchers.html')
    context = {
        # 'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))