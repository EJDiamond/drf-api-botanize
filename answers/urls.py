from django.urls import path
from answers import views

urlpatterns = [
    path('answers/', views.AnswerList.as_view()),
    path('answers/<int:pk>', views.AnswerDetail.as_view())
]
