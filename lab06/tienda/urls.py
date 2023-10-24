from django.urls import path

from . import views

app_name = 'tienda'

urlpatterns = [
    #path('', views.index,name='index'),
    #path('producto/<int:producto_id>/', views.producto, name='producto'),
    #path('categoria/<int:categoria_id>/',views.categoria,name='categoria'),
    path('',views.IndexView.as_view(),name='index'),
    path('categoria',views.SeriesViewCategoria.as_view(),name='categorias'),
    path('categoria/<int:serie_id>',views.SerieDetailViewCategoria.as_view()),
    path('producto',views.SeriesViewProducto.as_view(),name='productos'),
    path('producto/<int:serie_id>',views.SerieDetailViewProducto.as_view()),

]
