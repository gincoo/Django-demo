from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/',views.detail,name='detail'),
    # ex: /polls/5/results
    path('<int:question_id>/results/',views.result,name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote')
]