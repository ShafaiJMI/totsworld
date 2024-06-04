from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.signin,name="login"),
    path('signup/',views.signup,name="signup"),
    path('signout/',views.signout,name="signout"),
    path('activate/<uidb64>/<token>/',views.activate,name="activate"),
    path('reset_password/<uidb64>/<token>/',views.resetpassword,name="resetpassword"),
    path('change_password/<uidb64>/<token>/',views.changepassword,name="changepassword"),

]