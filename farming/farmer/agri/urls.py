from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # In urls.py
    path('login/home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('news/', views.news_view, name='news'),
    path('contact/', views.contact_view, name='contact'),
    path('farming/', views.farming_views, name='farming'),
    path('shop/', views.shop_views, name='shop'),
    path('ourproduct/', views.ourproduct_views, name='ourproduct'),
    path('bestfarmers/', views.bestfarmers_views, name='bestfarmers'),
    path('weather/', views.weather_views, name='weather'),
    path('signup/', views.signup, name='signup'),
    path('signup/login', views.login, name='login'),
    path('saveenquiry/', views.saveEnquiry, name='saveenquiry'),
    path('farming/aprentice/', views.aprenticeship, name='aprenticeship'),
    path('cart/', views.cart_page, name='cart_page'),
    path('pay/', views.pay, name='pay'),
    path('logout/index/', views.index, name='logout'),
    path('login/', views.login, name='login'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="passreset_complete.html"),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="passreset_email.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="passreset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="passreset_done.html"),name="password_reset_complete"),



]
