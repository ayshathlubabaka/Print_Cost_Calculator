from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import re
from django.core.exceptions import ValidationError

# Create your views here.

def signin(request):
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
                    messages.success(request, "Login successful.")
                    return render(request, 'index.html')  # Redirect or render success page
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