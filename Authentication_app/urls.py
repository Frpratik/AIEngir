from django.urls import path
from .views import RegisterView, VerifyView, LoginView, LogoutView, MeView, get_csrf

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('register/verify/', VerifyView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('me/', MeView.as_view()),
    path('csrf/', get_csrf),
]
