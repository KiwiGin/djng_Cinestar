from django.urls import path, include
from rest_framework import routers
from project import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'cines-api', views.CineViewSet)
router.register(r'peliculas-api', views.PeliculaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.home, name='home'),
    path('cines/', views.getCines, name='cines'),
    path('cines/<int:idcine>/', views.getCine, name='cine'),
    path('peliculas/cartelera/', views.getPeliculas, {'tipo': 'cartelera'}, name='peliculas_cartelera'),
    path('peliculas/cartelera/<int:idpelicula>/', views.getPelicula, name='pelicula'),
    path('peliculas/estrenos/', views.getPeliculas, {'tipo': 'estrenos'}, name='peliculas_estrenos'),
    path('peliculas/estrenos/<int:idpelicula>/', views.getPelicula, name='pelicula'),
    path('peliculas/<int:idpelicula>/', views.getPelicula, name='pelicula')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
