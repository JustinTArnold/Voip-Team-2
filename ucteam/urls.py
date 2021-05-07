from django.contrib import admin  
from django.urls import path, include
from django.conf.urls import url
from ucteamapp import views  
from django.views.generic.base import TemplateView

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('hello/', views.hello),
    path('inventory/save_table', views.save_table, name='save_table'),  
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('inventory/', TemplateView.as_view(template_name='inventory.html'), name='inventory'),
    path('accounts/', include('django.contrib.auth.urls'))
]  