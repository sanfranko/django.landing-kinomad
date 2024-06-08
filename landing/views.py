from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"Имя: {name}\nПочта: {email}\n\nСообщение:\n{message}"

        try:
            send_mail(
                f'Новая заявка от {name}',
                full_message,
                settings.EMAIL_HOST_USER,
                [settings.ADMIN_EMAIL, 'sanfrankooo3@gmail.com'],
                fail_silently=False,
            )
            return redirect('success')
        except Exception as e:
            print(f"Error sending email: {e}")
            return render(request, 'index.html', {'error': 'There was an error sending your message. Please try again later.'})
    return render(request, 'landing/index.html')

def success(request):
    return render(request, 'landing/success.html')
