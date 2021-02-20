from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('academy/', views.AcademyListView.as_view(), name='academy'),
                  path('academy/<int:pk>', views.AcademyDetailView.as_view(), name='academy-detail'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
