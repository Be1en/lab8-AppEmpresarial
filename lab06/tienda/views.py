from django.shortcuts import get_object_or_404, render

from .models import Producto, Categoria
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CategoriaSerializer, ProductoSerializer

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias = Categoria.objects.order_by('nombre')
    context = {'product_list':product_list, 'category_list': categorias}
    return render(request,'index.html',context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk = producto_id)
    categorias = Categoria.objects.order_by('nombre')[:6]
    return render(request,'producto.html', {'producto': producto,'category_list': categorias})

def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk = categoria_id)
    product_list = Producto.objects.filter(categoria=categoria).order_by('nombre')
    categorias = Categoria.objects.order_by('nombre')[:6]
    return render(request,'categoria.html', {'product_list': product_list,'category_list': categorias})





#CATEGORIAS

class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class SeriesViewCategoria(APIView):
    
    def get(self,request):
        dataCategorias = Categoria.objects.all()
        serCategorias = CategoriaSerializer(dataCategorias, many=True)
        return Response(serCategorias.data)



    def post(self,request):
        serCategorias = CategoriaSerializer(data=request.data)
        serCategorias.is_valid(raise_exception=True)
        serCategorias.save()
        return Response(serCategorias.data)
    
class SerieDetailViewCategoria(APIView):
    
    def get(self,request,serie_id):
        dataCategorias = Categoria.objects.get(pk=serie_id)
        serCategorias = CategoriaSerializer(dataCategorias)
        return Response(serCategorias.data)

    
    def put(self,request,serie_id):
        dataCategorias = Categoria.objects.get(pk=serie_id)
        serCategorias = CategoriaSerializer(dataCategorias,data=request.data)
        serCategorias.is_valid(raise_exception=True)
        serCategorias.save()
        return Response(serCategorias.data)
    
    def delete(self,request,serie_id):
        dataCategorias = Categoria.objects.get(pk=serie_id)
        serCategorias = CategoriaSerializer(dataCategorias)
        dataCategorias.delete()
        return Response(serCategorias.data)

#PRODUCTOS

    
class SeriesViewProducto(APIView):
    
    def get(self,request):
        dataProductos = Producto.objects.all()
        serProductos = ProductoSerializer(dataProductos,many=True)
        return Response(serProductos.data)
    
    def post(self,request):
        serProductos = ProductoSerializer(data=request.data)
        serProductos.is_valid(raise_exception=True)
        serProductos.save()
        
        return Response(serProductos.data)
    
class SerieDetailViewProducto(APIView):
    
    def get(self,request,serie_id):
        dataProductos = Producto.objects.get(pk=serie_id)
        serProductos = ProductoSerializer(dataProductos)
        return Response(serProductos.data)
    
    def put(self,request,serie_id):
        dataProductos = Producto.objects.get(pk=serie_id)
        serProductos = ProductoSerializer(dataProductos,data=request.data)
        serProductos.is_valid(raise_exception=True)
        serProductos.save()
        return Response(serProductos.data)
    
    def delete(self,request,serie_id):
        dataProductos = Producto.objects.get(pk=serie_id)
        serProductos = ProductoSerializer(dataProductos)
        dataProductos.delete()
        return Response(serProductos.data)