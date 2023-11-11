import random
def lectura():
    with open("productos.txt") as productosTxt:
        productosStr = productosTxt.read() #Lee el Txt con productos y lo vuelve string

    contador = 0
    listaProd = []
    char = ""
    newChar = ""
    nuevaLista = []

    for i in productosStr: #Recorre el string anterior, si encuentra un salto de linea lo reemplaza con una coma para separar el producto actual con el producto que viene. 
        if i == "\n":
            char += ","
        else:
            char += i #Deja el string como esta, pero en lugar de saltos de linea entre prodcutos, hay comas. 

    for i in char: 
        if i != ",":
            newChar += i
        else: #Va a buscar cuando encuentra comas en el str 
            nuevaLista.append(newChar) #Cuando encuentra una coma, añade el precio o el nombre del producto (que esta entre comas) a una nueva lsita (con el nombre y los dos valores del producto).
            newChar = "" 
            contador += 1
            if contador % 3 == 0 and contador != 1: #Cuando conto tres comas, añade la nueva lsita (del producto con su valor) a una lista final con todos los productos. 
                listaProd.append(nuevaLista)
                nuevaLista = [] #Se renueva la nueva lista para el siguiente producto.

    return listaProd
#print(lectura())

def buscar_producto(listaProd):
    indiceRandom = random.randrange(0,len(listaProd)+1) #Selecciona un indice aleatorio de la lista de todos los productos. 
    prodRandom = listaProd[indiceRandom] #Busca el indice aleatorio en la lista y se lo asigna a productoRandom
    premiumOEconomico = random.randrange(1, 3) #Da un indice random (1 o 2) para decidir si se va a usar el precio premium (guardado en el indice 2 del producto) o economico

    if premiumOEconomico == 1 : #En base al indice anterior, se asigna al producto "economico" o "premium" dependiendo de que precio se va a usar
        prodRandomPrice = [prodRandom[0], "(economico)", prodRandom[1]] 
    else :
        prodRandomPrice = [prodRandom[0], "(premium)", prodRandom[2]]
    return prodRandomPrice #Retornamos una lista con un producto aleatorio, con un precio aleatorio (entre premium o economico)
# print(buscar_producto(lectura()))