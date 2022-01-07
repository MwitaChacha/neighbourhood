from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
   path('',views.index, name='index'),
   path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html')),
   path('update-profile',views.update_profile, name='update_profile'), 
   path('profile/<pk>',views.profile, name = 'profile'),  
]