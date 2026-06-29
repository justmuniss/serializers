from django.urls import  path

from page import views

urlpatterns = [
    path('list/', views.CarAPIView.as_view()),
    path('create/', views.CarCreateAPIView.as_view()),
]