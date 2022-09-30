#blog/urls.py
from django.urls import path
from .views import VistaDetallePublicacion, VistaEliminarBlog, VistaListaBlog, VistaCrearBlog, VistaEditarBlog, VistaEliminarBlog

urlpatterns = [
    path('', VistaListaBlog.as_view(), name='inicio'),
    path('pub/<int:pk>/', VistaDetallePublicacion.as_view(), name='detalle_pub'),
    path('pub/nueva/', VistaCrearBlog.as_view(), name='nueva_publicacion'),
    path('pub/<int:pk>/editar/', VistaEditarBlog.as_view(), name='editar_publicacion'),
    path('pub/<int:pk>/eliminar/', VistaEliminarBlog.as_view(), name ='eliminar_publicacion'),
    
]