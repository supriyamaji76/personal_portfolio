from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from base.models import Contact, Project, Skill
from django.conf import settings

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    categories = {
        'Languages': skills.filter(category='Language'),
        'Technologies': skills.filter(category='Technology'),
        'Courses': skills.filter(category='Course'),
        'Database': skills.filter(category='Database'),
    }

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
            # Save contact to DB
            Contact.objects.create(name=name, email=email, number=number, content=content)

            # Send email to yourself
            subject = f"📬 New Contact from {name}"
            message = f"""
            You received a new contact form submission:

            Name: {name}
            Email: {email}
            Phone: {number}

            Message:
            {content}
            """
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = ['supriyamaji76@gmail.com']  # Replace with your email

            try:
                send_mail(subject, message, from_email, to_email)
                messages.success(request, 'Thank you for contacting me! Your message has been saved and emailed.')
            except Exception as e:
                messages.error(request, f'Message saved, but email failed: {str(e)}')

        return redirect(reverse('home') + '#contact')

    return render(request, 'home.html', {
        'projects': projects,
        'categories': categories
    })
