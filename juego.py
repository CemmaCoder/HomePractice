import random

def jugar():
    user = input("Escoge una opcion: \n 'Pi' para piedra, 'Pa' para papel, 'Ti' para tijera,  \n").lower()
    computer = random.choice(['pi', 'pa', 'ti'])

    if user == computer:
        return '¡EMPATE!'
    if winUser(user,computer):
        return '¡GANASTE!'
    else:
        return '¡PERDISTE!'
    

def winUser(user, computer):
    if ((user=="pi" and computer=="ti") 
        or (user=="pa" and computer=="pi")
        or (user=="ti" and computer=="pa")):
        return True

print(jugar())