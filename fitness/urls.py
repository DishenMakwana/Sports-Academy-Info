from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('fitness/', views.FitnessListView.as_view(), name='fitness'),
                  path('club/<int:pk>', views.FitnessDetailView.as_view(), name='fitness-detail'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
