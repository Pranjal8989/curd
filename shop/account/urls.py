from django.urls import path
from account import views
urlpatterns = [
    # path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('Logout/',views.Logout,name='Logout'),
 
]