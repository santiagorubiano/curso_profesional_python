# class Even_numbers:
#         def __init__ (self, max):
#                 self.max=max
#         def __iter__ (self,max):
#                 self.num=0
#                 return self
#         def __next__(self):
#                 if not self.max or self.num <=self.max:
#                         result=self.num
#                         self.num +=2
#                         return result
#                 else:
#                         raise StopIteration





# #Creando un iterador
# my_list = [1,2,3,4,5]  #tenemos una lista del 1 al 5 
# my_iter = iter(my_list) #tenemos el iterador llamado my_iter que es el resultado de aplicar la funcion iter sobre la lista 

#         #iterando un iterador
# while True: #cicli while infinoto, por que le pasamos true
#         try:#clausulas try, except para el manejo de errores
#                 element=next(my_iter)# sacamos el siguiente elemrnto del iteredor con la funcion next
#                 print(element) # y se guarda en una variable llamada element
#         except StopIteration:#en caso que haya error StopIteration sale un breack
#                 break
         


        #cuando no quedan datos,las excepcion StopIteration es elevada
        
# my_list = [1,2,3,4,5]  #tenemos una lista del 1 al 5 
# for element in my_list:
#         print(element)
        
# from tkinter import S


# empty_set= {}
# empty_set1= set()
# print(type(empty_set))
# print(type(empty_set1))


# set1={1,2,3,4,5}
# set2={5,6,7}

# set3= set1|set2
# print(set3)


set1={1,2,3,4,5}
set2={5,6,7}
set3 = set1 ^ set2
print(set3) 
