lista=[1,2,3,4]
def maior(lista):
    
    if len(lista) ==2:
        return lista[0] if lista[0]>lista[1] else lista[1]    
    sub_max=maior(lista[1:])
    return lista[0]if lista[0]> sub_max else sub_max

print(maior(lista))