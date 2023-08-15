

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from school import views, HOD_views, Staff_views
from school import Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='BASE'),

    #login
    path('', views.Login, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='doLogout'),


    #Profile Update URL
    path('profile', views.Profile, name='profile'),
    path('profile/update', views.profile_update, name='profile_update'),
    ##HOD panel
    path('HOD/Home', HOD_views.Home, name='hod_home'),
    path('HOD/Student/Add', HOD_views.Add_student, name='add_student')

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
