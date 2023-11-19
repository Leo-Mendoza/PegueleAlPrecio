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
    prodRandom = listaProd[ random.randint( 0 , len(listaProd) -1 ) ] #Selecciona un idnice aleatorio de la lista ed productos y elige ese producto
    premiumOEconomico = random.randint(1, 2) #Da un indice random (1 o 2) para decidir si se va a usar el precio premium (guardado en el indice 2 del producto) o economico

    if premiumOEconomico == 1 : #En base al indice anterior, se asigna al producto "economico" o "premium" dependiendo de que precio se va a usar
        prodRandomPrice = [prodRandom[0], "(economico)", prodRandom[1]] 
    else :
        prodRandomPrice = [prodRandom[0], "(premium)", prodRandom[2]]
    return prodRandomPrice #Retornamos una lista con un producto aleatorio, con un precio aleatorio (entre premium o economico)
# print(buscar_producto(lectura()))

def dameProducto(listaProd, margen): 
    while True: #Creamos un ciclo infinito donde generaremos 3 productos aleatoriamente hasta que encontremos el correcto
        prod1 = buscar_producto(listaProd) 
        prod2 = buscar_producto(listaProd)  
        prod3 = buscar_producto(listaProd)

        #Comparamos la diferencia de precios entre los 3 productos. El primero que encontremos que tenga una diferencia de precios menor al margen (respecto de los otros 2 productos), sera el que usemos
        if abs(prod1[2] - prod2[2]) <= margen and abs(prod1[2] - prod3[2]) <= margen: 
            return prod1    
        if abs(prod2[2] - prod1[2]) <= margen and abs(prod2[2] - prod3[2]) <= margen:
            return prod2
        if abs(prod3[2] - prod1[2]) <= margen and abs(prod3[2] - prod2[2]) <= margen:
            return prod3
# print(dameProducto(lectura(), 1000))

def esUnPrecioValido(precio,listaProd,margen):
    cont = 0
    for elem in listaProd:
        if abs(elem[1] - precio) <= margen or abs(elem[2] - precio) <= margen : #Se fija que haya productos que tengan menos que el margen de diferencia con el precio
            cont += 1
            if cont == 3: #Si hay 3 de esos productos, retorno true
                return True
    return False
# print(esUnPrecioValido(183, lectura(),1000))

def procesar(prodPrincipal, prodCandidato, margen):
    if abs(prodPrincipal[2] - prodCandidato[2]) <= margen:  #Busca que haya una diferencia menor al margen entre el precio del produto y el precio del candidato
        return prodCandidato[2] #Si la diferencia es menor al margen, retorna el precio del candidato
    else: return 0 #Caso contrario, retorna 0


def sonProductosDiferentes(listaDeProductosAleatorios):
    listaParaComparar = listaDeProductosAleatorios  #Tengo dos listas, una que me dieron por parametro, y una para comparar
    productos = 0
    for elem in listaDeProductosAleatorios:
        for prod in listaParaComparar:
            if  elem[0] == prod[0]:
                productos +=1   #Cada vez que yo encuentro un producto de la lista que me pasaron en la lista de comparacion, sumo 1.
    if productos == len(listaDeProductosAleatorios): return True #Si ninguno de los productos se repitio, el largo de la lista y la cantidad de productos que encontre deben ser iguales 
    else: return False #Si el largo de la lista es diferente de la cantidad de productos que conte, hay mas productos, o sea, alguno de ellos esta repetido y por ende son iguales

def dameProductosAleatorios(producto, listaProd, margen):
    while True: #Hago un ciclo infinito en caso de no encontrar productos con un precio similar reiniciar el ciclo
        prod1 = buscar_producto(listaProd)  #Busco 5 productos aleatorios, que aleatoriamente tengan precio economico o premium
        prod2 = buscar_producto(listaProd)
        prod3 = buscar_producto(listaProd)
        prod4 = buscar_producto(listaProd)
        prod5 = buscar_producto(listaProd)
        cont = 0
        prodAleatorios = [producto, prod1, prod2, prod3, prod4, prod5]
        if sonProductosDiferentes(prodAleatorios): #Me aseguro de que ninguno de los productos aleatorios por chance sean iguales entre si, o iguales al producto que me dieron por parametro
            if abs(producto[2] - prod1[2]) <= margen: #Con cada producto verifico si esta dentro o no del margen. 
                cont+=1 
            if abs(producto[2] - prod2[2]) <= margen:
                cont+=1
            if abs(producto[2] - prod3[2]) <= margen:
                cont+=1
            if abs(producto[2] - prod4[2]) <= margen:
                cont+=1
            if abs(producto[2] - prod5[2]) <= margen:
                cont+=1

            if cont >= 2: #Si hay como minimo 2 productos dentro del margen, retorno toda la lista. Quizas haya mas de 2 productos aleatorioamente
                return [producto, prod1, prod2, prod3, prod4, prod5]
print(dameProductosAleatorios(["Refrigerador", "(premium)", 4533], lectura(), 1000))    