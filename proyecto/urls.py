"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from bebidas.views import *
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static

handler404= error_404
handler500= error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('empresa/', empresa, name='empresa'),
    path('buscar/', buscar, name='buscar'),
    path('contacto/', contacto, name='contacto'),
    path('registro/', usuario_nuevo, name='registro'),
    path('privado/', privado, name='privado'),
    path('ingresar/', ingresar, name='ingresar'),
    path('salir/', salir, name='salir'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)