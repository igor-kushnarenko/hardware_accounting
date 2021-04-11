from django.urls import path

from users.views import login_view, AlternativeLoginView


urlpatterns = [
    path('login/', login_view, name='login'),
    # дополнительная форма авторизации сделаная с помощью специальной вьюхи LoginView. Чисто для теста.
    path('alternative_login/', AlternativeLoginView.as_view(), name='alternative_login'),
]