import random
def lectura():
    with open("productos.txt") as productosTxt:
        productosStr = productosTxt.read() #Lee el Txt con productos y lo vuelve string

    producto = []
    char = ""
    listaProductos = []

    for i in productosStr:
        if i != "\n" and i != ",": #Guarda temporalmente todo lo que haya antes de una coma o salto de linea
            char += i
        else: 
            producto.append(char) #Cuando encuentra una coma o un salto de linea, guarda las letras o cifras que recorrio hasta el momento en una lista del producto individual
            char = ""
            if i == "\n": #Si es un salto de linea, guarda esa lista del producto en una lista de todos los productos, y continua buscando mas
                producto[1], producto[2] = int(producto[1]), int(producto[2]) #Convierte los strings de precio de producto en numeros antes de guardarlos
                listaProductos.append(producto)
                producto = []

    return listaProductos #Retorna una lista de listas (lista de productos individuales con su nombre y precios)
# print(lectura())

def buscar_producto(listaProd):
    indiceRandom = random.randint(0,len(listaProd)-1) #Selecciona un indice aleatorio de la lista de todos los productos. 
    prodRandom = listaProd[indiceRandom] #Busca el indice aleatorio en la lista y se lo asigna a productoRandom
    premiumOEconomico = random.randint(1, 2) #Da un indice random (1 o 2) para decidir si se va a usar el precio premium (guardado en el indice 2 del producto) o economico

    if premiumOEconomico == 1 : #En base al indice anterior, se asigna al producto "economico" o "premium" dependiendo de que precio se va a usar
        prodRandomPrice = [prodRandom[0], "(economico)", prodRandom[1]] 
    else :
        prodRandomPrice = [prodRandom[0], "(premium)", prodRandom[2]]
    return prodRandomPrice #Retornamos una lista con un producto aleatorio, con un precio aleatorio (entre premium o economico)
# print(buscar_producto(lectura()))

def damePorducto(listaProd, margen):
    buscando = True
    while buscando: #Creamos un ciclo infinito donde generaremos 3 productos aleatoriamente hasta que encontremos el correcto
        prod1 = buscar_producto(lectura()) 
        prod2 = buscar_producto(lectura())  
        prod3 = buscar_producto(lectura())

        #Comparamos la diferencia de precios entre los 3 productos. El primero que encontremos que tenga una diferencia de precios menor al margen (respecto de los otros 2 productos), sera el que usemos
        if abs(prod1[2] - prod2[2]) <= margen and abs(prod1[2] - prod3[2]) <= margen: 
            return prod1    
        if abs(prod2[2] - prod1[2]) <= margen and abs(prod2[2] - prod3[2]) <= margen:
            return prod2
        if abs(prod3[2] - prod1[2]) <= margen and abs(prod3[2] - prod2[2]) <= margen:
            return prod3

print(damePorducto(lectura(), 1000))