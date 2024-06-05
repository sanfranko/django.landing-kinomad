from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Отправка письма (можно настроить по своему усмотрению)
            send_mail(
                f'New contact form submission from {name}',
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL, 'sanfrankooo3@gmail.com'],  # Замените на ваш email
                fail_silently=False,
            )
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'landing/index.html', {'form': form})


def success(request):
    return render(request, 'landing/success.html')
