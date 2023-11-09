from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail

import random
import string

from .models import UserProfile

from django_registration.forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Деактивируем пользователя
            user.save()

            # Генерируем и сохраняем код подтверждения
            confirmation_code = generate_confirmation_code()
            profile = UserProfile(user=user, confirmation_code=confirmation_code)
            profile.save()

            # Отправляем код подтверждения по электронной почте
            send_confirmation_email(user.email, confirmation_code)

            return redirect('activation')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def generate_confirmation_code():
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(10))
    return code


def send_confirmation_email(email, confirmation_code):
    subject = 'Подтверждение регистрации'
    message = (f'Ваш код подтверждения: {confirmation_code}')
    from_email = 'noreply@example.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)