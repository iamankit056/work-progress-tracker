from django.urls import path
from works import views

urlpatterns = [
    path('', views.home, name='home_url'),
]
