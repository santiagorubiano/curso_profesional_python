
print("""________________BIENVENIDO_________________
INGRESA UNA OPCION POR FAVOR:
1.Encontrar raiz cuadrada del numero ingresado con busqueda binaria
2.Encontrar raiz cuadrada del numero ingresado con busqueda por aproximacion
3.Encontrar raiz cuadrada del numero ingresado con busqueda por unumeracion exhastiva

4 salir 👻
    """)
def menu():
    opcion_m=int(input("ingrese una opcion: "))
    if opcion_m ==1:
        b_binaria()
    elif opcion_m==2:
        b_aproximacion()
    elif opcion_m==3:
        b_enumeracion()
    else:
        exit

def b_binaria():
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def b_enumeracion():
    objetivo = int(input('Escoge un entero: '))
    respuesta = 0

    while respuesta**2 < objetivo:
         print(respuesta)
         respuesta += 1

    if respuesta**2 == objetivo:
         print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')
    
        
def b_aproximacion():
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.1
    paso = epsilon**2 
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cudrada de {objetivo} es {respuesta}')  



def run():
 menu()

if __name__=="__main__":
    run()
    
    


