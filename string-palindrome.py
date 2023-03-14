# Problema: dada una cadena de Python, compruebe si es o no un palíndromo.

def palindrome(normal):
    reverse = normal[::-1]
    if(normal==reverse):
        # return True
        print("True")
    else:
        # return False
        print("False")

palindrome("ala")
palindrome("river")