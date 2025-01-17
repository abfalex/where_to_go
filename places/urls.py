from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from places import views

urlpatterns = [
    path("", views.home),
    path("places/<int:place_id>", views.generate_place, name="generate_place"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
