from django.urls import path
from .views import *

app_name = 'contactus'

urlpatterns = [
    path('' , ContactUsView.as_view() , name='contactus_main')
]