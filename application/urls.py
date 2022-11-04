from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('charts', views.charts, name='charts'),
    path('vouchers', views.vouchers, name='vouchers'),
    path('postvoucher', views.postvoucher, name='postvoucher'),
    path('admission', views.admission, name='admission'),
    path('student', views.student, name='student'),
    path('fetch_students', views.fetch_students, name='fetch_students'),
    path('clear_device', views.clear_device, name='clear_device'),
    path('post_to_device_students', views.post_to_device_students, name='post_to_device_students'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]