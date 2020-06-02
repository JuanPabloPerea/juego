"""

int+int<=21
funcion ganar


"""

from random import shuffle

"""_________________________________________________________________"""


def baraja():
    
    return [(n, p) for n in ['A','2','3','4','5','6','7','8','9','10','J','Q','K'] for p in ['corazones','picas','treboles','diamantes']]


"""_________________________________________________________________"""


def mezclar(baraja):
    
    shuffle(baraja)
    return baraja


"""_________________________________________________________________"""


def sacar_carta(baraja):
    
    if baraja == []:
        pass
    else:
        print(baraja[0], valor_carta(baraja[0]))
        
        sacar_carta(baraja[1:])
        
        
"""_________________________________________________________________"""



def valor_carta(carta):
    
    if carta[0] in ['J','Q','K']:
        return 10
    elif carta[0]=='A':
        return 1
    elif carta[0] in ['2','3','4','5','6','7','8','9','10']:
        return int(carta[0])
    

"""_________________________________________________________________"""



def valor_mano(mano):
    
    if mano == []:      
        return 0   
    else:
        return valor_carta(mano[0])+valor_mano(mano[1:])
    

"""_________________________________________________________________"""



def valor_mano_recargado(mano):
    
    if valor_mano(mano) <= 11 and 1 in [valor_carta(x) for x in mano]:      
        return valor_mano(mano) + 10
    else:
        return valor_mano(mano)




"""_____________________________    JUEGO    ____________________________"""




def jugar(mazo, jugador, repartidor,ini):


    if((jugador == []) and (repartidor == [])):

        jugar(mazo[2:], jugador+[mazo[0]], repartidor+[mazo[1]], 0)

        
    if int(ini) == 0:

        if((jugador != []) and (repartidor != [])):

            print("El mazo del jugador es: " + str(jugador) + " con un valor de " + str(valor_mano_recargado(jugador)))

            

            if(valor_mano_recargado(jugador) == 21):
                print("sopas1")
                print("conseguiste 21")

                jugar(mazo[1:], jugador, repartidor, 1)

            elif(valor_mano_recargado(jugador) >= 21):
                print("sopas2")
                print("te pasaste de 21")
    
                jugar(mazo[1:], jugador, repartidor, 1)
                
            elif(valor_mano_recargado(jugador) <= 21):
                print("sopas3")                    
                ini = input("Quieres otra carta (0): ")
                
                if((int(ini) == 0) and (len(mazo) > 2)):
                    print("sopas")
    
                    jugar(mazo[1:], jugador+[mazo[0]], repartidor, 0)


    if int(ini) == 1:

        if((jugador != [])&(repartidor != [])):
        
            print("El mazo del repartidor es: " + str(repartidor) + " con un valor de " + str(valor_mano_recargado(repartidor)))

            if(valor_mano_recargado(repartidor) == 21):

                print("conseguiste 21")

                jugar(mazo[1:], jugador, repartidor, 2)

            elif(valor_mano_recargado(repartidor) >= 21):

                print("te pasaste de 21")
    
                jugar(mazo[1:], jugador, repartidor, 2)

            elif(valor_mano_recargado(repartidor) <= 21):

                ini = input("Quieres otra carta (1): ")

                if((int(ini) == 1) and (len(mazo) > 2)):

                    jugar(mazo[1:], jugador, repartidor+[mazo[0]], 1)
                    
    if int(ini) == 2:
        
        if(valor_mano_recargado(jugador) > valor_mano_recargado(repartidor)):
            
            print("gana el jugador")
            
        elif(valor_mano_recargado(jugador) < valor_mano_recargado(repartidor)):
            
            print("gana el repartidor")
            
        elif(valor_mano_recargado(jugador) == valor_mano_recargado(repartidor)):
            
            print("gana el repartidor")
            
                
    
    

jugar(mezclar(baraja()), [], [], 1)





"""
juego(mezclar(baraja()))
x = input("")




while():
 
    jugar(mezclar(baraja()), [], [], 0)






def jugar(mazo, jugador, repartidor):
    
    print (jugador, repartidor)

    if len(mazo) > 2:

        jugar(mazo[2:],jugador+[mazo[0]],repartidor+[mazo[1]])







print(valor_mano(mezclar(baraja())[:2]))

"""





