from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def resume(request):
    return render(request,'resume.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"""
        Name: {name}
        Email: {email}
        Message:
        {message}
        """

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            ['your_email@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, "Message has been sent Succcessfully")
        return redirect('/contact/')

       

    return render(request, "contact.html")