from rest_framework import serializers
from .models import Cine, Pelicula, Cinepelicula, Cinetarifa, Distrito, Genero

class DistritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distrito
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['detalle']

class CineSerializer(serializers.ModelSerializer):
    distrito = serializers.StringRelatedField(source='iddistrito.detalle', read_only=True)

    class Meta:
        model = Cine
        fields = ['id', 'razonsocial', 'salas', 'direccion', 'telefonos', 'distrito']

class PeliculaSerializer(serializers.ModelSerializer):
    generos_nombres = serializers.SerializerMethodField()

    class Meta:
        model = Pelicula
        fields = ['id', 'titulo', 'fechaestreno', 'director', 'generos_nombres', 'idclasificacion', 'idestado', 'duracion', 'link', 'reparto', 'sinopsis']

    def get_generos_nombres(self, obj):
        generos = obj.generos
        generos_ids = generos.split(',')
        nombres = []
        for genero_id in generos_ids:
            genero = Genero.objects.get(id=int(genero_id))
            nombres.append(genero.detalle)
        return ', '.join(nombres)

class CinepeliculaSerializer(serializers.ModelSerializer):
    titulo = serializers.StringRelatedField(source='idpelicula.titulo', read_only=True)

    class Meta:
        model = Cinepelicula
        fields = ['titulo', 'horarios']

class CinetarifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinetarifa
        fields = ['diassemana', 'precio']