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

#print(readTest())