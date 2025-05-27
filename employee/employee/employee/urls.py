
from django.contrib import admin
from django.urls import path
from optima import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view),
    path('powerbi_dashboard', views.powerbi_dashboard, name='powerbi_dashboard'),
]


