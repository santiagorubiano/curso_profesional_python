def es_primo(numero:int)->bool:
    contador=0
    for i in range(1,numero+1) :
        
        if numero==1:
            return False
        if i ==1 or i == numero:
            continue
        if numero%i == numero:
            contador+=1
    if  contador==0:
        return True
            
    else:
            return False

def run():
    print(es_primo(3))
    print(es_primo("a"))





if __name__== "__main__":
    run()