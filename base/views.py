from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from base.models import Contact, Project, Skill

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    categories = {
        'Languages': skills.filter(category='Language'),
        'Technologies': skills.filter(category='Technology'),
        'Courses': skills.filter(category='Course'),
        'Database': skills.filter(category='Database'),
    }

    # Handle POST request from contact form
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')

        # Validations
        if not (2 < len(name) < 30):
            messages.error(request, 'Length of name should be between 3 and 29 characters.')
        elif not (5 < len(email) < 40) or '@' not in email:
            messages.error(request, 'Invalid email. Please try again.')
        elif not number.isdigit() or not (10 <= len(number) <= 12):
            messages.error(request, 'Invalid number. Please enter a valid number.')
        elif not (5 <= len(content) <= 500):
            messages.error(request, 'Message must be between 5 and 500 characters.')
        else:
            # Save the message
            Contact.objects.create(name=name, email=email, number=number, content=content)
            messages.success(request, 'Thank you for contacting me! Your message has been saved.')

        # Always redirect to contact section after POST (even on validation errors)
        return redirect(reverse('home') + '#contact')

    # For GET request
    return render(request, 'home.html', {
        'projects': projects,
        'categories': categories
    })
