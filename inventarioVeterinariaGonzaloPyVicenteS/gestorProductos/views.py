from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm

# Create your views here.

def gestor_productos(request):
    return render(request, 'gestorProductos/gestorProductos.html')

# creacion del crud
# creacion de requerimientos para visualizar

#PRODUCTOS

@login_required
def lista_productos(request):
    if request.user.is_superuser:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(usuario=request.user)
    return render(request, 'gestorProductos/lista_productos.html', {'productos': productos})

@login_required
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'gestorProductos/detalle_producto.html', {'producto': producto})

@login_required
def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm()
    return render(request, 'gestorProductos/editar_producto.html', {'form': form})

@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'gestorProductos/editar_producto.html', {'form': form})

@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk) #si no encuentra la soliciutud manda error 404
    if request.user.is_superuser:
        producto.delete()
    return redirect('lista_productos')

#CATEGORIAS

@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'gestorProductos/categorias/lista_categorias.html', {'categorias': categorias})

@login_required
def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'gestorProductos/categorias/editar_categoria.html', {'form': form})

@login_required
def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'gestorProductos/categorias/editar_categoria.html', {'form': form})

@login_required
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.user.is_superuser:
        categoria.delete()
    return redirect('lista_categorias')

@login_required
def detalle_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'gestorProductos/categorias/detalle_categoria.html', {'categoria': categoria})
