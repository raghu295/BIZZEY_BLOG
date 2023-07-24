from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages

from blog.helper import save_file
from blog.models import Profile, Blog, User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.admin.views.decorators import user_passes_test

# Create your views here.

def home(request):
    message = "Hello Everyone Welcome to my Blogging Page"
    context = {"message": message}
    # set value on session
    request.session["blog"] = "Welcome to my Blogging Page"
    return render(request, "home.html", context)



def log_in(request):
    if request.method == "POST":
        email_id = request.POST.get("email")
        password = request.POST.get("password")
        print(f"Email: {email_id}, Password: {password} ")
        # check if email exist in database
        if not User.objects.filter(email = email_id).exists():
            messages.error(request, message="Email does not exists")
            return redirect("login")
        # check if email or password is correct
        user_query = User.objects.get(email=email_id)
        username = None
        if user_query:
            username = user_query.username     # get user from user table
        user = authenticate(request, username =username, password= password)
        if user is not None:
            login(request, user)
            profile_pic = None
            if Profile.objects.filter(user__email=request.user.email).exists():
                profile_pic = Profile.objects.get(user__email=request.user.email).profile_image
            request.session["profile_pic"] = profile_pic
            return redirect("profile_page")

        else:
            messages.error(request, message="Email or Password is incorrect")
            return redirect("login")
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

        if User.objects.filter(email = email_id).exists():
            messages.error(request, message="Email already exists")
            return redirect("register")

        # insert profile to databse
        user_data = {"username": email_id, "email": email_id, "password": password}
        user = User.objects.create(**user_data)
        user.set_password(password)
        user.save()
        profile_data = {"user": user, "firstname": first_name, "lastname": last_name}
        profile = Profile.objects.create(**profile_data)
        return redirect("login")
    return render(request, "register.html")


def about(request):
    return render(request, "about.html")

def contact(request):
    # get vlaue on session
    print("request.session:", request.session.get("blog"))
    return render(request, "contact.html")


def blog(request):
    search_string = request.GET.get("q")
    print("search_string:", search_string)
    if search_string:
        blog = Blog.objects.filter(title__icontains=search_string)
    else:
        blog = Blog.objects.all().order_by("-created_at")
    has_data = len(blog) > 0
    page_number = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 2)
    paginator = Paginator(blog, per_page)
    blog_with_pagination = paginator.get_page(page_number)
    context = {"blog_with_pagination": blog_with_pagination, "per_page": per_page, "has_data": has_data}
    return render(request, "blog.html", context)

@login_required
@user_passes_test(lambda user: user.is_superuser)
def create_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        blog_image = request.FILES.get("blog_image")
        image_url = save_file(request, blog_image)
        blog_data = {"title": title, "description": content, "image": image_url, "user": request.user}
        print(blog_data)
        Blog.objects.create(**blog_data)    # insert data to database table blog
        return redirect("blog")
    return render(request, "create_blog.html")

@login_required
def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {"blog": blog}
    return render(request, "blog-single.html", context)


def log_out(request):
    logout(request)
    return HttpResponseRedirect("/login")

@login_required
@user_passes_test(lambda user: user.is_superuser)
def blog_delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    messages.info(request, message="Blog deleted Successfully")
    return redirect("blog")



@login_required
@user_passes_test(lambda user: user.is_superuser)
def blog_update(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("content")
        blog_image = request.FILES.get("blog_image")
        image_url = save_file(request, blog_image)


        if title:
            blog.title = title
        if description:
            blog.description = description
        if image_url:
            blog.image = image_url
        blog.save()
        messages.info(request, message="Blog updated Successfully")
        return redirect("blog")
    return render(request, "edit-blog.html", {"blog": blog})


@login_required
def profile_page(request):
    # get value on session
    print("request.session:", request.session.get("blog"))
    profile = {}
    if Profile.objects.filter(user__email=request.user.email).exists():
        profile = Profile.objects.get(user__email=request.user.email)
        if request.method == "POST":
            contact = request.POST.get("contact")
            address = request.POST.get("address")
            profile_image = request.FILES.get("profile_image")
            if profile_image:
                profile_image_url = save_file(request, profile_image)
                profile.profile_image = profile_image_url
            if contact:
                profile.contact = contact
            if address:
                profile.address = address
            profile.save()
            messages.info(request, message="Profile updated Successfully")
            return redirect("profile_page")
    context = {"profile": profile}
    return render(request, "profile.html", context)