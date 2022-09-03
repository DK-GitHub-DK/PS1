from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('s_signup', views.s_signup, name='s_signup'),
    path('s_login', views.s_login, name='s_login'),
    path('portal', views.portal, name='portal')
]