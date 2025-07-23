from django.urls import path , re_path , include
from . import views


app_name = 'account'


urlpatterns = [
    path('otp_registeration' , views.OtpRegisterationView.as_view() , name="otp"),
    path('check_otp' , views.CheckOtpCode.as_view() , name="check_otp"),
    path('logout' , views.logout_user , name="logout"),
    path('profile' , views.ProfileView.as_view() , name="profile"),
    path('edit_profile' , views.profile_edite , name="edit_profile"),
    path('add/address' , views.AddAdressView.as_view() , name="add_address"),
    path('edit/address/<int:pk>' , views.address_edite , name="edit_address"),
    path('address' , views.AddressListView.as_view() , name='address'),
    path('delete/address/<int:id>' , views.DeleteAddressView.as_view() , name='delete_address'),
    path('wishlist' , views.WishListView.as_view() , name='whishlist'),
    path('order' , views.OrderListView.as_view() , name='orderlist'),
    path('order-detail/<int:pk>' , views.OrderDetailView.as_view() , name='orderdetail'),
    path('order_admin' , views.AdminOrderList.as_view() , name='admin_order'),
]
