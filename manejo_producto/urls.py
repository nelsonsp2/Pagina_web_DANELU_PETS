from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from proyectazo.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('todos_productos/', views.estanteria, name='estanteria'),
    path('publicar_pro/', views.publicar , name='modificar_producto'),
    path('modificar_pro/<int:id_producto>', views.modificar),
    path('eliminar_pro/<int:id_producto>', views.eliminar),
]
if DEBUG:
    urlpatterns += static(STATIC_URL,document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)