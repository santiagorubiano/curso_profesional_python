def make_division_by(n:int)->int:
    def division(x:int)->int:
        assert type(x)==int, "solo se pueden ingresar numeros enteros"
        return x/n
    return division
def run():
    division_by_3 = make_division_by(3)
    print(int(division_by_3(18)))

    division_by_5 = make_division_by(5)
    print(int(division_by_5(100)))

    division_by_18 = make_division_by(18)
    print(int(division_by_18(54)))

    
    
    
if __name__=="__main__":
    run()