from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render

from users.forms import AuthForm


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('http://127.0.0.1:8000/hardwares/')
                else:
                    auth_form.add_error('__all__', 'Пользователь не найден в системе!')
            else:
                auth_form.add_error('__all__', 'Проверьте правильность написания логина!')
    else:
        auth_form = AuthForm()
    context = {'form': auth_form}
    return render(request, 'users/login.html', context=context)


class AlternativeLoginView(LoginView):
    template_name = 'users/login.html'