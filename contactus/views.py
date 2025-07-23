from django.shortcuts import redirect, render
from django.views.generic import View
from .models import *

class ContactUsView(View):
    template_name = 'contactus/contactus.html'
    def get(self , request):
        contact_info = ContactInfo.objects.all()
        return render(self.request , self.template_name , {'contact':contact_info})
    def post(self , request):
        contact_info = ContactInfo.objects.all()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        sub_title = request.POST.get('sub_title')
        message = request.POST.get('message')
        Contact.objects.create(name=name , phone=phone , sub_title=sub_title , message=message)
        return redirect('home:main')