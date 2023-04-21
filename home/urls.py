from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('signin',views.signin,name="signin"),
    path("signin_verification",views.signin_verification,name="signin_verification"),
    path("send_otp",views.send_otp,name="send_otp"),
    path("otp_verification",views.otp_verification,name="otp_verification"),
    path("user_login",views.user_login,name="user_login"),
    path("verify",views.verify,name="verify"),
    path("district_views",views.district_views,name="district_views"),
    path("center",views.center,name="center"),
    path("booking",views.booking,name="booking"),
    path("logout",views.logout,name="logout")
]