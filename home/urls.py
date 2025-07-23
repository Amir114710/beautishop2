from django.urls import path
from .views import * 

app_name = 'home'

urlpatterns = [
    path('' , HomeView.as_view() , name='main'),
    path('faq' , FaqView.as_view() , name='faq'),
    path('cunstomer' , CustomerClubView.as_view() , name='customer'),
    path('law' , LawView.as_view() , name='law'),
]