"""
URL configuration for ecommerce_project project.

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
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings

from api.views import run_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Подключаем маршруты API из приложения api
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Эндпоинт для получения JWT токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Эндпоинт для обновления токена
    path('run-task/', run_task, name='run_task'),
    path('', include('django_prometheus.urls')),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
