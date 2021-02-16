from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import RedirectView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index, name='index'),
                  path('about/', views.about, name='about'),
                  path('classes/', views.classes, name='classes'),
                  path('sports/', include('sports.urls')),
                  path('', RedirectView.as_view(url='/sports/', permanent=True)),
                  path('', RedirectView.as_view(url='/fitness/', permanent=True)),
                  path('', RedirectView.as_view(url='/yoga/', permanent=True)),
                  path('fitness/', include('fitness.urls')),
                  path('yoga/', include('yoga.urls')),
                  # path('user/', include('user.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path("register/", views.register, name="register"),
    # path("accounts/password_reset/", views.password_reset_request, name="password_reset_req"),
]
