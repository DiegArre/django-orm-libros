from django.urls import path
from . import views

urlpatterns = [
    path("",views.start),
    path("libros", views.libros),
    path("autores",views.autores),
    path("añadir/<str:here>",views.añadir),
    path("libro/<int:el_id>",views.mostrar_libro),
    path("autor/<int:el_id>",views.mostrar_autor)
]
