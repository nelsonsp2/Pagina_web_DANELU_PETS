
from django.urls import path
from . import views
from proyectazo.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload-Domiciliario'),
    path('update/<int:Domiciliario_id>', views.update_Domiciliario),
    path('delete/<int:Domiciliario_id>', views.delete_Domiciliario),
]
if DEBUG:
    urlpatterns += static(STATIC_URL,document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)