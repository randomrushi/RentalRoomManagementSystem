from django.contrib import admin
from django.urls import path,include
from Mainapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home , name='home'),
    path('login/',views.login , name='login'),
    path('login/login_tenant',views.login_tenant , name='login_tenant'),
    path('login/register_tenant',views.register_tenant,name="register_tenant"),
    path('login/register_owner',views.register_owner,name="register_owner"),
    path('profile_tenant/',views.tenant_profile ,name='tenant_profile'),
    path('profile_owner/',views.owner_profile , name='owner_profile'),
    path('aboutus/',views.aboutus , name='aboutus'),
    path('owner/',views.owner , name='owner'),
    path('tenant/',views.tenant , name='tenant'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)