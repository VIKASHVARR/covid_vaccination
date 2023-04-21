from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('india',views.india,name="india"),
    path('foreign',views.foreign,name='foreign'),
    path('signin',views.signin,name='signin'),
    path('login',views.login,name="login"),
    path('verify',views.verify,name="verify"),
    path('signin_verification',views.signin_verification,name="signin_verification"),
    path('otp',views.otp,name="opt"),
    path("send_otp",views.send_otp,name="send_otp"),
    path('logout',views.logout,name="logout"),
    path("user",views.user,name="user"),
    path('booking',views.booking,name="booking"),
    path('fbooking',views.fbooking,name="fbooking"),
    path("contact",views.contact,name="contact"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("payment",views.payment,name="payment"),
    path("success",views.success,name="success"),
    path("failure",views.failure,name="failure")
]