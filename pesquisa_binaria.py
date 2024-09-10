minha_lista=[3,7,12,6,19,2,4,1,8,17,23,24,85,96,27,38]
def pesquisa_binario(lista,item):
    baixo = 0
    alto=len(lista)-1
    while baixo<=alto:
        meio=(baixo+alto)//2
        chute=lista[meio]
        if chute==item:
            return meio
        if chute>item:
            alto=meio-1
        else:
            baixo=meio+1
    return None

print (pesquisa_binario(minha_lista,23))
print (pesquisa_binario(minha_lista,8))
print (pesquisa_binario(minha_lista,3))
