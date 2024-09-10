lista=[1,2,3,4]
def contagem(lista):
    total=0
    if lista ==[]:
        return 0    
    return 1+contagem(lista[1:])
    

print(contagem(lista))