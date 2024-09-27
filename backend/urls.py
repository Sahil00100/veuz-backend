"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from rest_framework_simplejwt import views as jwt_views
from authentication.views import Signup
from dashboard.views import dashboard,employee_settings,employee_view

urlpatterns = [
    path('admin/', admin.site.urls),

    #auth sec
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    #authentication
    path('signup/', Signup, name='Signup'),

    #dashbioard
    path('dashboard/', dashboard, name='dashboard'),
    path('employee-settings/', employee_settings, name='employee_settings'),
    path('employee_view/', employee_view, name='employee_view'),

]
