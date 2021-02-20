from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('center/', views.YogaListView.as_view(), name='center'),
                  path('center/<int:pk>', views.YogaDetailView.as_view(), name='yoga-detail'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
