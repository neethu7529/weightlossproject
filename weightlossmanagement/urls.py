"""
URL configuration for weightlossmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from weightloss import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', views.login_page, name='login'),
    path('', views.weightloss, name='home'),
    path('about-us/', views.about, name='about-us'),
    path('addWeight/', views.addWeight, name='addWeight'),
    path('addedWeight/', views.addedWeight, name='addedWeight'),
    path('update/<int:pk>/', views.weight_update, name='update'),
    path('delete/<int:pk>/', views.weight_delete, name='delete'),
    path('weight-list/', views.weight_list, name='weight_list'),
    path('weight-loss/', views.weight_loss_calculator, name='weight_loss_calculator'),
    path('accounts/logout/', views.logout_page, name='logout'),
]