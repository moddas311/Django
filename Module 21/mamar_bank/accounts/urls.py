from django.urls import path
from .views import userRegistrationView, userLoginView, userLogoutView, userBankAccountUpdateView

urlpatterns = [
   path('register/', userRegistrationView.as_view(), name='register'),
   path('login/', userLoginView.as_view(), name='login'),
   path('logout/', userLogoutView.as_view(), name='logout'),
   path('profile/', userBankAccountUpdateView.as_view(), name='profile' )
   
]