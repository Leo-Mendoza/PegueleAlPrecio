import random
def lectura():
    with open("productos.txt") as productosTxt:
        productosStr = productosTxt.read() #Lee el Txt con productos y lo vuelve string

    producto = []
    char = ""
    listaProductos = []

    for i in productosStr:
        if i != "\n":
            if i != ",": #Empieza a guardar letra por letra todo el string hasta que se encuentre una coma
                char += i
            else:
                producto.append(char) #Cuando se encuentra una coma, suma todo lo que encontro hasta el momento (nombre o precio economico) en la lista del producto individual, reincia lo que encontro y sigue buscando la proxima coma o salto de linea
                char = ""
        else: #Cuando se encuentra un salto de linea, ya tiene guardado el ultimo precio (premium)
            producto.append(char) #Suma el precio premium a la lista del producto
            char = ""
            listaProductos.append(producto) #Guarda la lista del producto individual en la lista que contiene todos los producto
            producto = []  
    return listaProductos #Retorna una lista de listas (lista de productos individuales con su nombre y precios)
print(lectura())

def buscar_producto(listaProd):
    indiceRandom = random.randrange(0,len(listaProd)+1) #Selecciona un indice aleatorio de la lista de todos los productos. 
    prodRandom = listaProd[indiceRandom] #Busca el indice aleatorio en la lista y se lo asigna a productoRandom
    premiumOEconomico = random.randrange(1, 3) #Da un indice random (1 o 2) para decidir si se va a usar el precio premium (guardado en el indice 2 del producto) o economico

    if premiumOEconomico == 1 : #En base al indice anterior, se asigna al producto "economico" o "premium" dependiendo de que precio se va a usar
        prodRandomPrice = [prodRandom[0], "(economico)", prodRandom[1]] 
    else :
        prodRandomPrice = [prodRandom[0], "(premium)", prodRandom[2]]
    return prodRandomPrice #Retornamos una lista con un producto aleatorio, con un precio aleatorio (entre premium o economico)
print(buscar_producto(lectura()))