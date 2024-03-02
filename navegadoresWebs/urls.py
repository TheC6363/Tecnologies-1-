from django.urls import path

from navegadoresWebs.views import navegadores, CreacionNavegadores,ActualizarNavegadores,DetalleNavegador, EliminarNavegador

urlpatterns = [
    
    path("navegadores", navegadores.as_view(), name = "navegadores"),
    path("navegadores/crear", CreacionNavegadores.as_view(), name = "crear_navegador"),
    path("navegadores/<int:pk>/eliminar",EliminarNavegador.as_view() , name = "eliminar"),
    path("navegadores/<int:pk>/editar", ActualizarNavegadores.as_view(), name = "editar"),
    path("navegadores/<int:pk>/detalle", DetalleNavegador.as_view(), name = "detalle"),
    
]