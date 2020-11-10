from particula import Particula
import json

class Particula_libreria:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula) 

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str (particula) + '\n' for particula in self.__particulas
        )

    def __len__(self):
        return len(self.__particulas)

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration
        

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0


#l01 = Particula(origen_x=3, origen_y=5, destino_x=5, destino_y=9, velocidad=45, red=123, green=456, blue=789, distancia=0)
#l02 = Particula(3, 5, 5, 9, 45, 123, 456, 789, 0)
#particula_libreria = Particula_libreria()
#particula_libreria.agregar_final(l01)
#particula_libreria.agregar_inicio(l02)
#particula_libreria.agregar_inicio(101)
#particula_libreria.mostrar()  