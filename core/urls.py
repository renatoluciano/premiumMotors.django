from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Painel Administrativo nativo do Django
    path('admin/', admin.site.urls),
    
    # Rota principal da loja (Conecta diretamente ao app catalogo)
    path('', include('catalogo.urls')),
]

# Libera o acesso às fotos dos carros enviados pelo painel durante o desenvolvimento local
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
