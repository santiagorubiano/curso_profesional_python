def make_reapeater_of(n:int):
    def repeater(string:str):
        assert type(string)== str , "solo puedes utilizar cadenas"
        return string*n
    return repeater

def run():
    repeat_5= make_reapeater_of(5)
    print(repeat_5("Hola"))
    repeat_10=make_reapeater_of(10)
    print(repeat_10("Santiago Rubiano "))
    repeat_2 =make_reapeater_of(2)
    print(repeat_2("missy"))
    

    
    
if __name__== "__main__":
    run()