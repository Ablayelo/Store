from django.urls import path
from profiles import views

    
app_name = 'profile'   
urlpatterns = [
    path('profile/',views.profile, name='profile'),

]
  
