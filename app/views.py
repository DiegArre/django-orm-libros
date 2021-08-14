from django.shortcuts import redirect, render
from app.models import * 

# Create your views here.
def start(request): #por mientras
    return redirect("/libros")


def libros(request):
    print(Libro.objects.all())
    context = {

        "libros" : Libro.objects.all()

    }
    return render(request, "libros.html",context)

def autores(request):
    print(Autor.objects.all())
    context = {

        "autores" : Autor.objects.all()

    }
    return render(request, "autores.html",context)



def añadir(request,here):
    if request.method == "POST":

        if here == "libros":
            print(request.POST)

            nuevo_libro = Libro.objects.create(
                titulo = request.POST["titulo"],
                descripcion = request.POST["desc"]
            )


        if here == "autores":
            print(request.POST)

            nuevo_autor = Autor.objects.create(
                first_name = request.POST["nombre"],
                last_name = request.POST["apellido"],
                notas = request.POST["notas"]
            )

        return redirect(f"/{here}")

def mostrar_libro(request,el_id):
    libro = Libro.objects.get(id = el_id)
    print(set(libro.autores.all()))
    print(set(Autor.objects.all()))
    print(set(Autor.objects.all()) - set(libro.autores.all()))
    otros_autores = set(Autor.objects.all()) - set(libro.autores.all())
    context = {

        "libro" : Libro.objects.get(id = el_id),
        "autores_libro" : libro.autores.all(),
        "otros_autores" : otros_autores
    }

    if request.method == "POST":
        this_libro = Libro.objects.get(id=el_id)
        this_autor = Autor.objects.get(id=request.POST["id_autor"])
        this_libro.autores.add(this_autor)
        return redirect(f"/libro/{el_id}")

    return render(request,"detalle_libro.html",context)



def mostrar_autor(request,el_id):
    autor = Autor.objects.get(id = el_id)
    # print(set(autor.libros.all()))
    # print(set(Libro.objects.all()))
    # print(set(Libro.objects.all()) - set(autor.libros.all()))
    libros_otro_autor = set(Libro.objects.all()) - set(autor.libros.all())
    context = {

        "autor" : Autor.objects.get(id = el_id),
        "autor_libros" : autor.libros.all(),
        "otros_libros" : libros_otro_autor
    }

    if request.method == "POST":
        print(request.POST)
        this_autor = Autor.objects.get(id=el_id)
        this_libro = Libro.objects.get(id = request.POST["id_libro"])
        print(this_autor,this_libro)
        #Se añade el autor al libro
        this_autor.libros.add(this_libro)
        return redirect(f"/autor/{el_id}")


    return render(request,"detalle_autor.html",context)

def eliminar_libros(request,id_libro):
    libro_eliminar = Libro.objects.get(id=id_libro)
    libro_eliminar.delete()
    return redirect("/libros")
    
def eliminar_autores(request,id_autor):
    autor_eliminar = Autor.objects.get(id=id_autor)
    autor_eliminar.delete()
    return redirect("/autores")

def eliminar_autor_libro(request,id_autor,id_libro):
    this_autor = Autor.objects.get(id=id_autor)
    this_libro = Libro.objects.get(id=id_libro)

    this_libro.autores.remove(this_autor)

    return redirect(f"/libro/{id_libro}")

def eliminar_libro_autor(request,id_autor,id_libro):
    this_autor = Autor.objects.get(id=id_autor)
    this_libro = Libro.objects.get(id=id_libro)

    this_autor.libros.remove(this_libro)
    
    return redirect(f"/autor/{id_autor}")
    



