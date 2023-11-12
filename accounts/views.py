from django.shortcuts import redirect
from django.contrib.auth import login
from django.shortcuts import render

from .models import UserProfile


def confirm_registration(request):  # подтверждение регистрации
    # print(f'подтверждение регистрации')
    if request.method == 'POST':
        confirmation_code = request.POST.get('confirmation_code')
        user_profile = UserProfile.objects.get(confirmation_code=confirmation_code)
        user = user_profile.user
        user.is_active = True  # Активируем пользователя
        user_profile.save()
        user.save()
        #        print(f'Пользователь успешно активирован {user}')
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('posts')
    #    print(f'Пользователь не активирован {request.user}')
    return render(request, 'registration/confirm_registration.html')


