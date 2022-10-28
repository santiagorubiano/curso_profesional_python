class Even_Numbers:
# esta clase implementa un iterador de todos los numeros pares,
# o los numeros pares hasta un maximo.
    def __init__(self,max=None) -> None:
       self.max=max
#el atributo max de este objeto que mas adelante va a ser un
#iterador va a ser == al parametro max que me va a llegar al 
#iterador
    def __iter__(self):
        self.num=0
        return self
# le metodo __iter__ sirve para tener elementnos o atributos que 
# se necesita para que el iterador funcione
# en este caso lo unico que necesito como voy a imprimir todos los
# numeros pares es cada uno de los numeros de esa iteracion en este
#caso yo le pongo num de nombre y le asigono el valor de 0 el primer
# numero postosteriormente retorno el objeto en si mismo, convierto un
#iterable en un iterador 

    def __next__ (self):
        if not self.max or self.num <=self.max:
            result=self.num
            return result
        else:
            StopIteration
# es el que pemite extraer cada uno de los elementos de mi itedador 
#si no existeself.max o self.num es menor o igual <=self.max 
# le asigno a una variable result el valor de self.num despues
# le sumo 2 a self.num recordar que el atrivuto num  es el valor que va vuelta por vuelta
# entonces si al principio vale 0 despues 2 en cada vuelta se sumo dos y pot ultimo hagi un 
#return de result, por utimo tengo un else:
#lo que hace ese elevar el error StopIteration