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

def dameProducto(listaProd, margen): #Este es sin usar "listaprod" porque los saca directamente de buscar_producto asumiendo que es la misma lista
    while True: #Creamos un ciclo infinito donde generaremos 3 productos aleatoriamente hasta que encontremos el correcto
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
# # print(dameProducto(lectura(), 1000))

# def dameProducto2(listaProd, margen): #Esta version si usa listaProd
#     prodConPrecioSimilarABarato = 0
#     prodConPrecioSimilarAPremium = 0

#     while True: #Este ciclo se usa porque si no se encuentran dos productos con un precio similar al prodRandom, se elige otro prodRandom
#         prodRandom = listaProd[ random.randint( 0 , len(listaProd) -1 ) ]   #Elegimos un producto aleatorio de la lista
#         for elem in listaProd:
#             if abs(elem[1] - prodRandom[1]) <= margen or abs(elem[2] - prodRandom[1]) <= margen:    #Usando el precio barato de este producto aleatorio, vemos si hay algun otro producto en la lista con un precio similar
#                 prodConPrecioSimilarABarato += 1
#             if abs(elem[1] - prodRandom[2]) <= margen or abs(elem[2] - prodRandom[2]) <= margen:    #Verificamos lo mismo con el precio premium
#                 prodConPrecioSimilarAPremium += 1
            
#             if prodConPrecioSimilarABarato == 2:
#                 return [prodRandom[0], "(economico)", prodRandom[1]]    #Si hay 2 elementos con un precio similar al producto barato, enviamos el producto con el precio barato
#             if prodConPrecioSimilarAPremium == 2:
#                 return [prodRandom[0], "(premium)", prodRandom[2]]  #Si hay 2 elementos con un precio similar al producto premium, enviamos el producto premium
# # print(dameProducto2(lectura(), 1000))

def esUnPrecioValido(precio,listaProd,margen):
    cont = 0
    for elem in listaProd:
        if abs(elem[1] - precio) <= margen: #Se fija que haya productos que tengan menos que el margen de diferencia con el precio
            cont += 1
            if cont == 3: #Si hay 3 de esos productos, retorno true
                return True
    return False
# print(esUnPrecioValido(183, lectura(),1000))

def procesar(prodPrincipal, prodCandidato, margen):
    if abs(prodPrincipal[2] - prodCandidato[2]) <= margen:  #Busca que haya una diferencia menor al margen entre el precio del produto y el precio del candidato
        return prodCandidato[2] #Si la diferencia es menor al margen, retorna el precio del candidato
    else: return 0 #Caso contrario, retorna 0

def dameProductosAleatorios(producto, listaProd, margen):
    while True: #Hago un ciclo infinito en caso de no encontrar productos con un precio similar reiniciar el ciclo
        prod1 = buscar_producto(lectura())  #Busco 5 productos aleatorios
        prod2 = buscar_producto(lectura())
        prod3 = buscar_producto(lectura())
        prod4 = buscar_producto(lectura())
        prod5 = buscar_producto(lectura())

        if abs(producto[2] - prod1[2]) <= margen: #Si alguno de estos cinco productos aleatorios tienen un precio dentro del margen respecto al producto que me dieron, retorno toda la lista, con el produco que me dieron y el que encontre + los 4 aleatorios. 
            return [producto, prod1, prod2, prod3, prod4, prod5]
        if abs(producto[2] - prod2[2]) <= margen:
            return [producto, prod1, prod2, prod3, prod4, prod5]
        if abs(producto[2] - prod3[2]) <= margen:
            return [producto, prod1, prod2, prod3, prod4, prod5]
        if abs(producto[2] - prod4[2]) <= margen:
            return [producto, prod1, prod2, prod3, prod4, prod5]
        if abs(producto[2] - prod5[2]) <= margen:
            return [producto, prod1, prod2, prod3, prod4, prod5]
# #print(dameProductosAleatorios(["Refrigerador", "(premium)", 4533], lectura(), 1000))    