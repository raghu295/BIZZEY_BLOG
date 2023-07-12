from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def home(request):
    message = "Hello Everyone Welcome to my Blogging Page"
    context = {"message": message}
    return render(request, "home.html", context)



def login(request):
    if request.method == "POST":
        email_id = request.POST.get("email")
        password = request.POST.get("password")
        print(f"Email: {email_id}, Password: {password} ")
        return redirect("home")
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email_id = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        print(f"First Name: {first_name}, Last Name: {last_name}, Email: {email_id}, Password: {password}, Confirm Password: {confirm_password}")
        if password != confirm_password:
            messages.error(request, "Password and Confirm password does not match")
            return redirect("register")
        return redirect("login")
    return render(request, "register.html")


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


def blog(request):
    return render(request, "blog.html")

def create_blog(request):
    return render(request, "create_blog.html")


def blog_detail(request, blog_id):
    context = {"blog_id": 1}
    return render(request, "blog-single.html", context)
