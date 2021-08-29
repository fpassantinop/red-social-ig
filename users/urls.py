"""users urls"""

#Django
from django.urls import path

#views
from users import views

urlpatterns = [
    path(
        route='users/login/', 
        view=views.login_view, 
        name='login'),

    #management
    path(
        route='users/logout/', 
        view=views.logout_view, 
        name='logout'),
    path(
        route='users/signup/', 
        view=views.signup, 
        name='signup'),
    path(
        route='users/me/profile', 
        view=views.update_profile,
         name='update_profile')  
]


