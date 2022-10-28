from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):#*args no importa la cantidad de argumentos pisicionlaes que se le envien va a funcionar y
        initial_time=datetime.now() # el metodo now de datetime nos devuelve la fecha y hora exactas del momento que se ejecuta la linea de codigo
        func(*args, **kwargs)#**kwargs no importa la cantidad de argumentos nombrados laa funcion los va  a recibir
        final_time=datetime.now() # el metodo now de datetime nos devuelve la fecha y hora exactas del momento que se ejecuta la linea de codigo
        time_elapse=final_time- initial_time
        print("pasaron "+ str(time_elapse.total_seconds()) + "segundos") #el metodo totalsecons del objeto time_elapsenos permite la cantidad de segunods de la diferencia temporal que calculamos
        
    return wrapper
@execution_time
def ramdom_func():
     for _ in range(1,100000000):
         pass
@execution_time
def suma(a:int, b: int)->int:
    return a+b
@execution_time
def saludo(nombre="Santiago"):
    print("hola ",nombre.upper())
ramdom_func()
suma(10,100000000000000)
saludo("mafe")
# ramdom_func()
        
