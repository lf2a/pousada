# django
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# local django
from .views import deslogar, SignUp, error_404_view

urlpatterns = [
    # pousada amazon
    path('', include('quarto.urls')),
    path('reserva/', include('core.urls')),
    path('reservas/', include('cliente.urls')),

    # autenticacao
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', deslogar, name='logout'),

    # admin area
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'pousada.views.error_404_view'
