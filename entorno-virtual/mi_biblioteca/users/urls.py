from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='app_biblioteca/padre.html'), name="Logout"),
    path('edit/', views.editar_usuario, name="editarUsuario"),
]