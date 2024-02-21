
from django.contrib import admin
from django.urls import path, include
from inscription.views import inscription_home, inscription_client
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accueil.urls')),
    path('inscription/', include('inscription.urls') ),
    path('formulaire/', include('formulaire.urls') ),
    path('login/', include('login.urls') ),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
    
    urlpatterns += static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT)