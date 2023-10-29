from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from app.models import Students

# Create your views here.
def home(request):
    user = request,User
    student = Students.objects.all()
    return render(request,"home.html",{'username':user,'student':student})

def signuppage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("password2")
        if pass1 == pass2:
            myuser = User.objects.create_user(name,email,pass1)
            myuser.save()
            return redirect("loginpage")
        else:
            return redirect("signuppage")
        
    return render(request,"signup.html")
def loginpage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect("homepage")
        else:
            return redirect("loginpage")

    return render(request,"login.html")

# def addstudent(request):
#     if request.method == "POST":
#         username = request.POST.get("name")
#         firstname = request.POST.get("f_name")
#         lastname = request.POST.get("l_name")
#         email = request.POST.get("email")
#         mobile = request.POST.get("m_number")
#         profilepic = request.FILES.get("profilepic")

#         student = Students(
#             username = username,
#             first_name = firstname,
#             last_name = lastname,
#             email = email,
#             mobile_number = mobile,
#             profilepic = profilepic,
#         )
#         student.save()
#         return redirect("homepage")
#     return render(request,"addstudent.html")