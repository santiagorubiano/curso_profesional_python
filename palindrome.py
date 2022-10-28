import string
from xmlrpc.client import boolean

from pip import main


def is_palindrome(string:str)-> bool:
    string= string.replace(" ","").lower()
    return string== string[::-1]
def run():
    print(is_palindrome("Ana"))
    print(is_palindrome(111))
# lambda function 

palindrome = lambda string : string== string[::-1]
print(palindrome('ana'))
    
if __name__ =="__main__":
    run()