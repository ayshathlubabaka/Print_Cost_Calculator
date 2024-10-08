from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import re
from .models import CustomUser
from django.utils.translation import gettext as _
from .decorators import role_required

# Create your views here.

@role_required('superuser')
def create_user(request):
    email_error = None
    password_error = None
    role_error = None

    # Get the role choices from CustomUser model
    role_choices = dict(CustomUser.ROLE_CHOICES)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')  # Get the selected role

        try:
            # Validate email
            if not email:
                email_error = _("Email is required.")
            else:
                email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if not re.match(email_regex, email):
                    email_error = _("Invalid email format.")
                elif CustomUser.objects.filter(email=email).exists():
                    email_error = _("Email already registered.")

            # Validate password
            if not password:
                password_error = _("Password is required.")
            elif len(password) < 8:
                password_error = _("Password must be at least 8 characters long.")

            # Validate role
            if not role or role not in role_choices.keys():
                role_error = _("A valid role must be selected.")

            # If there are no errors, create the user
            if not email_error and not password_error and not role_error:
                user = CustomUser.objects.create_user(email=email, password=password, role=role)
                messages.success(request, _("User created successfully!"))
                return redirect('create_user')  # Redirect to admin dashboard or another appropriate page

        except Exception as e:
            messages.error(request, _('An unexpected error occurred. Please try again later.'))
            print(f"Error during user creation: {e}")  # Log the actual exception message

    return render(request, 'create_user.html', {
        'email_error': email_error,
        'password_error': password_error,
        'role_error': role_error,
        'role_choices': role_choices,  # Pass role choices to context
    })



def signin(request):
    if request.user.is_authenticated:
        user = request.user
        if user.role == 'superuser':
            return redirect('superuser_dashboard')  # Use redirect for better URL handling
        elif user.role == 'admin':
            return redirect('admin_dashboard')
        else:
            return redirect('user_dashboard')

    email = ""
    email_error = None
    password_error = None

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Validate email field
            if not email:
                email_error = "Email is required."
            else:
                email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if not re.match(email_regex, email):
                    email_error = "Invalid email format."

            # Validate password field
            if not password:
                password_error = "Password is required."

            # Check for errors before authenticating
            if not email_error and not password_error:
                # Authenticate user
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)

                    # Redirect users based on their role
                    if user.role == 'superuser':
                        return redirect('superuser_dashboard')
                    elif user.role == 'admin':
                        return redirect('admin_dashboard')
                    else:
                        return redirect('user_dashboard')
                else:
                    password_error = "Invalid email or password."

        except Exception as e:
            # Handle any unexpected errors
            messages.error(request, 'An unexpected error occurred. Please try again later.')
            print(f"Error during sign-in: {e}")

    # For GET requests or failed POST requests, render the form with errors
    context = {
        'email': email,
        'email_error': email_error,
        'password_error': password_error,
    }
    return render(request, 'index.html', context)

def user_dashboard(request):
    return render(request, 'user_dashboard.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def superuser_dashboard(request):
    return render(request, 'superuser_dashboard.html')

def signout(request):
    logout(request)  # Logs the user out
    return render(request, 'index.html') 