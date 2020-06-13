from django.urls import path
from django.conf.urls import url,re_path
from . import views

urlpatterns = [
    re_path('signUp', views.sign_up,name='sign_up'),
    re_path('^postSignUp', views.post_sign_up,name='post_sign_up'),
    re_path('postSignIn',views.post_sign_in,name='post_sign_in'),
   	re_path('signIn',views.sign_in,name='sign_in'),
   	re_path('^passwordReset',views.password_reset,name='password_reset'),
   	re_path('^postPasswordReset',views.post_password_reset,name='post_password_reset'),
   	re_path('^logOut',views.log_out,name='log_out'),
	re_path('^welcome',views.welcome,name='welcome'),

]