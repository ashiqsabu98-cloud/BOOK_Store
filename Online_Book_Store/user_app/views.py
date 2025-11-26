from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserLoginForm
from admin_app.models import Book, Category

# 🧍 Register
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login_user')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# 🔐 Login (redirect based on role)
'''
def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect based on user type
                if user.is_superuser:
                    return redirect('admin_dashboard')
                else:
                    return redirect('user_dashboard')
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

# 🚪 Logout
def logout_user(request):
    logout(request)
    return redirect('login_user')

# 👤 User Dashboard
@login_required
def user_dashboard(request):
    books = Book.objects.all()
    categories = Category.objects.all()

    context = {
        'user': request.user,
        'books': books,
        'categories': categories,
    }
    return render(request, 'user_dashboard.html', context)
'''

#new with session and cookies

def session_login(request):
   if request.method == "POST":
       username = request.POST.get('username') 
       password = request.POST.get('password') 

       try:
          user=User.objects.get(username=username)

          if user.check_password(password):
            request.session['user_id'] = user.id 
            request.session['username'] = user.username 
            request.session['email'] = user.email 
            response = redirect('session_dashboard') 
            response.set_cookie('username', user.username, max_age=3600)
            response.set_cookie('email', user.email, max_age=3600)
            return response
          else: 
                return HttpResponse("Invalid Password")
       except User.DoesNotExist: 
            return HttpResponse("User does not exist")
   return render(request, 'login.html')

def session_dashboard(request):
    username_session = request.session.get('username') 
    username_cookie=request.COOKIES.get('username')
    if 'username' in request.session:
        return render(request, 'dashboard.html',{'username': username_session,'cookie_user':username_cookie}) 
    else: 
        return redirect('session_login')
    
def session_logout(request):
    request.session.flush()
    return redirect('session_login')
