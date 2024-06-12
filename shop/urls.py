from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('tracker',views.tracker,name='tracker'),
    path('search',views.search,name='search'),
    path('product/<int:myid>',views.product,name='product'),
    path('checkout/',views.checkout,name='checkout'),
    path('login/',views.user_login,name='user_login'),
    path('signup/',views.signup, name='signup'),
    path('authenticated',views.authenticated, name='authenticated'),
    # path('verify-otp/', views.verify_otp, name='verify_otp'),
]
