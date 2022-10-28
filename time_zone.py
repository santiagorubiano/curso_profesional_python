# person_1_name=input("Escribe tu nombre: ")
# person_1_years=int(input("Escribe tu edad: "))
# person_2_name=input("Escribe tu nombre: ")
# person_2_years=int(input("Escribe tu edad: "))
# if person_1_years > person_2_years:
#     print(f"{person_1_name} es mayor que {person_2_name}")
# elif person_1_years < person_2_years:
#     print(f"{person_2_name} es mayor que {person_1_name}")
# else:
#     print(f"la edad de{person_1_name} y la edad de {person_2_name} es la misma")   
    
import time
def run():
    contador_horas = 24
    contador_minutos = 60
    contador_segundos=60
    while contador_horas !=0: 
        while contador_minutos !=0:
            while contador_segundos !=0:
                contador_segundos = contador_segundos -1
                print(f"horas: {contador_horas} minutos: {contador_minutos} Segundos: {contador_segundos} ")
                time.sleep(1)
    
       
            contador_minutos = contador_minutos -1
            contador_segundos=60
        contador_horas= contador_horas -1
        contador_minutos=60    
        
if __name__=="__main__":
    run()


    