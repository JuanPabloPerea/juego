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
        print(mano[0])
        return valor_carta(mano[0])+valor_mano(mano[1:])


"""_____________________________    JUEGO    ____________________________"""







"""  print(valor_mano(mezclar(baraja())[:a]))  """





