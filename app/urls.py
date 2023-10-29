from django.urls import path

from app import views

urlpatterns = [
    path('', views.signuppage,name="signuppage"),
    path('homepage', views.home,name="homepage"),
    path('loginpage', views.loginpage,name="loginpage"),
    path('addstudent', views.addstudent,name="addstudent"),
    path('deletestudent<int:id>', views.deletestudent,name="deletestudent"),
    path('updatestudent<int:id>', views.updatestudent,name="updatestudent"),
 
]
