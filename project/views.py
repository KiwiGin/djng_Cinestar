from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cine, Pelicula, Cinepelicula, Cinetarifa, Distrito, Genero
from .serializer import CineSerializer, PeliculaSerializer, CinepeliculaSerializer, CinetarifaSerializer, DistritoSerializer, GeneroSerializer
from django.shortcuts import render
import requests

class CineViewSet(viewsets.ModelViewSet):
    queryset = Cine.objects.all()
    serializer_class = CineSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class CinepeliculaListView(APIView):
    def get(self, request, idcine):
        cinepeliculas = Cinepelicula.objects.filter(idcine=idcine)
        serializer = CinepeliculaSerializer(cinepeliculas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CinetarifaListView(APIView):
    def get(self, request, idcine):
        cinetarifas = Cinetarifa.objects.filter(idcine=idcine)
        serializer = CinetarifaSerializer(cinetarifas, many=True)
        return Response(serializer.data)

class DistritoViewSet(viewsets.ModelViewSet):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

def home(request):
    return render(request, 'index.html')

def getCines(request):
    response = requests.get('http://localhost:8000/cinestar/bayes/cines-api/')
    cines = response.json()
    return render(request, 'cines.html', {'cines': cines})

def getCine(request, idcine):
    response_cine = requests.get(f'http://localhost:8000/cinestar/bayes/cines-api/{idcine}/')
    cine = response_cine.json()
    
    response_tarifas = requests.get(f'http://localhost:8000/cinestar/bayes/cinetarifa-api/{idcine}/')
    tarifas = response_tarifas.json()

    response_peliculas = requests.get(f'http://localhost:8000/cinestar/bayes/cinepelicula-api/{idcine}/')
    peliculas = response_peliculas.json()
    
    return render(request, 'cine.html', {'cine': cine, 'tarifas': tarifas, 'peliculas': peliculas})

def getPeliculas(request, tipo):
    response = requests.get('http://localhost:8000/cinestar/bayes/peliculas-api/')
    peliculas = response.json()
    if tipo == 'cartelera':
        peliculas = [p for p in peliculas if p['idestado'] == 1]
    elif tipo == 'estrenos':
        peliculas = [p for p in peliculas if p['idestado'] == 2]
    return render(request, 'peliculas.html', {'peliculas': peliculas})

def getPelicula(request, idpelicula):
    response = requests.get(f'http://localhost:8000/cinestar/bayes/peliculas-api/{idpelicula}/')
    pelicula = response.json()

    return render(request, 'pelicula.html', {'pelicula': pelicula})