class Pelicula:             #definimos una clase con atributo privado
    def __init__(self, nombre, director, genero):
        self.__nombre = nombre
        self.director = director
        self.genero = genero

    @property   #utilizamos un decorador para acceder al atributo __nombre
    def nombre(self):
        return self.__nombre
    
    @nombre.setter  #utilizamos decorador para asignar otro valor a nombre
    def nombre(self, nuevo_nombre):
        if nuevo_nombre:
            self.__nombre = nuevo_nombre
        else:
            raise ValueError("El nombre no puede estar vacío")  #detenemos la ejecucion del programa si el usuario ingresa espacios vacios

    def __str__(self):
        return f"{self.__nombre} Dirigida por: {self.director} Género: {self.genero}"   #retornamos los datos de nuestra clase
    
    import os #modulo para poder eliminar archivo