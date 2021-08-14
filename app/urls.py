from django.urls import path
from . import views

urlpatterns = [
    path("",views.start),
    path("libros", views.libros),
    path("autores",views.autores),
    path("añadir/<str:here>",views.añadir),
    path("libro/<int:el_id>",views.mostrar_libro),
    path("autor/<int:el_id>",views.mostrar_autor),
    path("libro/<int:id_libro>/eliminar/<int:id_autor>",views.eliminar_autor_libro),
    path("autor/<int:id_autor>/eliminar/<int:id_libro>",views.eliminar_libro_autor),
    path("autor/eliminar/<int:id_autor>",views.eliminar_autores),
    path("libro/eliminar/<int:id_libro>",views.eliminar_libros)
    
]
