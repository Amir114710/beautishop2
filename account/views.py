from django.shortcuts import get_object_or_404, render , redirect , reverse
from django.views.generic import FormView , TemplateView , CreateView , View , ListView
from uuid import uuid4
from cart.models import Order
from mixins import LoginRequirdMixins , LogoutRequirdMixins , AddressRequirdMixins
from django.urls import reverse_lazy
from django.contrib.auth import login , authenticate , logout
import ghasedakpack
import requests
from .form import RegisterForm , OtpForm , Edite_Profile_Form , AddressCreationForm
from random import randint
from .models import OTP, User , Address

sms = ghasedakpack.Ghasedak("a04c97fefa995b72fcbb1d9ab1b699569a367fef6026039499900c3e601c3a8c")

class OtpRegisterationView(LoginRequirdMixins , FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home:main')
    def form_valid(self, form):
        cd = form.cleaned_data
        random_code = randint(1000 , 9999)
        sms.verification({'receptor': cd['phone'] , 'type': '1','template': 'resinabeat','param1': random_code})
        token = str(uuid4())
        next_page = self.request.GET.get('next')
        OTP.objects.create(phone = cd['phone'] , code = random_code , token = token , next_page=next_page)
        print(random_code)
        return redirect(reverse('account:check_otp') + f'?token={token}')

class CheckOtpCode(LoginRequirdMixins , FormView):
    template_name = 'account/otp_form.html'
    form_class = OtpForm
    success_url = reverse_lazy('account:edit_profile')
    def form_valid(self, form):
        token = self.request.GET.get('token')
        cd = form.cleaned_data
        if OTP.objects.filter(code=cd['code'],token=token).exists():
            otp = OTP.objects.get(token=token)
            user , is_created = User.objects.get_or_create(phone = otp.phone)
            login(self.request , user)
            otp.delete()
            if otp.next_page:
                return redirect(otp.next_page)
            return redirect('account:edit_profile')       
        else:
            form.add_error(cd['code'] , 'this information is not correct')
        return render(self.request , self.template_name , {'form':form})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse('home:main'))
    else:
        return redirect(reverse('home:main'))


class ProfileView(LogoutRequirdMixins , TemplateView) :
    template_name = 'account/profile.html'


def profile_edite(request):
    if request.user.is_authenticated == True:
        user = request.user
        form = Edite_Profile_Form(instance=user)
        if request.method == 'POST':
            form = Edite_Profile_Form(request.POST  , request.FILES ,instance=user)
            if form.is_valid():
                form.save()
                return redirect('account:profile')
        else:
            form = Edite_Profile_Form(instance=user)
        return render(request , 'account/edit_profile.html' , {'form':form})
    else:
        return redirect('home_app:home')
    
class AddAdressView(AddressRequirdMixins , View):
    def post(self , request):
        form = AddressCreationForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            return redirect('account:address')
        return redirect('account:address')

    def get(self , request):
        form = AddressCreationForm()
        return render(request , 'account/add_address.html' , {'form':form})

def address_edite(request , pk):
    if request.user.is_authenticated == True:
        address = get_object_or_404(Address , id=pk)
        form = AddressCreationForm(instance=address)
        if request.method == 'POST':
            form = AddressCreationForm(request.POST  , request.FILES ,instance=address)
            if form.is_valid():
                address = form.save(commit=False)
                address.user = request.user
                address.save()
                return redirect('account:profile')
        else:
            form = AddressCreationForm(instance=address)
        return render(request , 'account/edit_address.html' , {'form':form})
    else:
        return redirect('home_app:home')
         
class AddressListView(AddressRequirdMixins , ListView):
    template_name = 'account/addresses.html'
    model = Address
    context_object_name = 'addresses'

class DeleteAddressView(AddressRequirdMixins ,View):
    def get(self , request , id):
        address = get_object_or_404(Address , id=id)
        address.delete()
        return redirect('account:address')
    
class WishListView(AddressRequirdMixins , View):
    template_name = 'account/whishlist.html'
    def get(self , request):
        wishes = request.user.user_favorite.all()
        return render(request , self.template_name , {'wishes':wishes})
    
class OrderListView(AddressRequirdMixins , TemplateView):
    template_name = 'account/order.html'
    
class OrderDetailView(AddressRequirdMixins , View):
    template_name = 'account/order-detail.html'
    def get(self , request , pk):
        order = get_object_or_404(Order , id=pk)
        return render(request , self.template_name , {'order':order})
    
class AdminOrderList(AddressRequirdMixins , ListView):
    template_name = 'account/orderlist_admin.html'
    model = Order
    context_object_name = 'orders'