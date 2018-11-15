from django.urls import path
from . import views

app_name = 'marketapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.index, name='index'),
    path('items/<int:item_id>/', views.detail, name= 'detail'),
    path('users/<int:user_id>/', views.user_page, name='user page')
]
