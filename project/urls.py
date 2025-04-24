# São as importações realizadas de forma a utilizar parte do django.
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# Lista responsável por organizar as urls do sistema.
urlpatterns = [
    path('', include('sistema.urls')),
    path('admin/', admin.site.urls),
]

# path() -> é um método do django que permite a inserção de uma url.

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)