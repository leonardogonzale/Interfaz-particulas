from algoritmos import distancia_euclidiana
class Particula:
    def __init__(self,Id=0, origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0,rojo=0, verde=0,azul=0, distancia=0):
        self.__Id =Id
        self.__origen_x =origen_x
        self.__origen_y =origen_y
        self.__destino_x =destino_x
        self.__destino_y =destino_y
        self.__velocidad =velocidad
        self.__rojo =rojo
        self.__verde =verde
        self.__azul =azul
        self.__distancia = distancia_euclidiana(origen_x,destino_x,origen_y,destino_y)

    def __str__(self):
        return (
            'Id:' + str(self.__Id) + '\n' +
            'origen_x:' + str(self.__origen_x) + '\n' +
            'origen_y:' + str(self.__origen_y) + '\n' +
            'destino_x:' + str(self.__destino_x) + '\n' +
            'destino_y:' + str(self.__destino_y) + '\n' +
            'velocidad:' + str(self.__velocidad) + '\n' +
            'rojo:' + str(self.__rojo) + '\n' +
            'verde:' + str(self.__verde) + '\n' +
            'azul:' + str(self.__azul) + '\n' +
            'distancia = ' + str(self.__distancia) + '\n'
        )  

    @property
    def Id(self):
        return self.__Id
    
    @property
    def origen_x(self):
        return self.__origen_x

    @property
    def origen_y(self):
        return self.__origen_y

    @property
    def destino_x(self):
        return self.__destino_x

    @property
    def destino_y(self):
        return self.__destino_y

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def rojo(self):
        return self.__rojo

    @property
    def verde(self):
        return self.__verde

    @property
    def azul(self):
        return self.__azul

    @property
    def distancia(self):
        return self.__distancia


    def to_dict(self):
        return{
            "Id":  self.__Id ,
	        "origen_x": self.__origen_x,
	        "origen_y":  self.__origen_y,
        	"destino_x": self.__destino_x,
        	"destino_y": self.__destino_y,
	        "velocidad": self.__velocidad,
	        "rojo": self.__rojo,
	        "verde": self.__verde,
	        "azul": self.__azul,
            "distancia": self.__distancia
        } 