from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [

    #  django에서 지원하는 url 패턴

    # ex:/polls/
    path('',views.IndexView.as_view(), name='index'),
    # ex:/polls/5/
    path('<int:pk>/',views.DetailView.as_view(), name='detail'),
    # ex:/polls/5/results/
    path('<int:pk>/results/',views.ResultsView.as_view(),name="results"),
    # ex:/polls/5/vote/
    path('<int:question_id>/vote/',views.vote,name='vote'),
]