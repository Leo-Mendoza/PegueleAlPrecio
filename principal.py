#! /usr/bin/env python
import os
import random
import sys
import math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesRESUELTAS import *
from extras import *

#Con codigo de leo
#Cargo las imagenes para los botones y la escalo a un tamaño apropiado
boton_imagen = pygame.image.load("imagenes\marco-verde.png")
boton_imagen = pygame.transform.scale(boton_imagen, (500,100))
boton_elegido_imagen = pygame.image.load("imagenes\marco-azul.png")
boton_elegido_imagen = pygame.transform.scale(boton_elegido_imagen, (500,100))

def main():
    # Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    
    #Preparamos los sonidos
    pygame.mixer.init()
    erro = pygame.mixer.Sound("quit.mp3")
    tecla = pygame.mixer.Sound("tecla.mp3")
    correcto = pygame.mixer.Sound("correcto.mp3")
    
    #defino el texto en el borde de la ventana
    pygame.font.init() #REVISAR

    # Preparar la ventana
    pygame.display.set_caption("Peguele al precio")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    #Cargo las imagenes para los botones y la escalo a un tamaño apropiado
    # boton_imagen = pygame.image.load("imagenes\marco-verde.png")
    # boton_imagen = pygame.transform.scale(boton_imagen, (500,100))
    # boton_elegido_imagen = pygame.image.load("imagenes\marco-azul.png")
    # boton_elegido_imagen = pygame.transform.scale(boton_elegido_imagen, (500,100))

    # tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0  # puntos o dinero acumulado por el jugador
    producto_candidato = ""

    #Lee el archivo y devuelve una lista con los productos,
    lista_productos = lectura()  # lista de productos

    # Elegir un producto, [producto, calidad, precio]
    producto = dameProducto(lista_productos, MARGEN)

    # Elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio.
    # De manera aleatoria se debera tomar el valor economico o el valor premium.
    # Agregar  '(economico)' o '(premium)' y el precio
    productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)
    # print(productos_en_pantalla)

    # la funcion dibu muestra tanto el producto principal como el timer y el score
    dibu(screen,productos_en_pantalla,producto,producto_candidato,puntos,segundos)
    
    #la funcion asignar botones devuelve una lista de botones configurados y listos para su uso
    lista_botones = asignar_botones(productos_en_pantalla,boton_imagen,producto)

    # dibuja la pantalla la primera vez
    # dibujar(screen, productos_en_pantalla, producto,
    #         producto_candidato, puntos, segundos)

    while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        posicion_mouse = pygame.mouse.get_pos()

        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return ()

            # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                tecla.play()
                letra = dameLetraApretada(e.key)
                producto_candidato += letra  # va concatenando las letras que escribe
                if e.key == K_BACKSPACE:
                    # borra la ultima
                    producto_candidato = producto_candidato[0:len(producto_candidato)-1]
                if e.key == K_RETURN:  # presionó enter
                    indice = int(producto_candidato)
                    # chequeamos si el prducto no es el producto principal. Si no lo es procesamos el producto
                    if indice < len(productos_en_pantalla) and indice != 0:
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        #Si procesar no retorna 0, esto significa que el usuario sumo puntos. Reproducimos un sonido de "acierto"
                        if procesar(producto, productos_en_pantalla[indice], MARGEN) != 0:
                            correcto.play()
                        if procesar(producto, productos_en_pantalla[indice], MARGEN) == 0:
                            erro.play()
                        producto_candidato = ""
                        # Elegir un producto
                        producto = dameProducto(lista_productos, MARGEN)
                        # elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio
                        productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)
                    else:
                        producto_candidato = ""
            #si el evento es el click
            if e.type == pygame.MOUSEBUTTONDOWN:
                #si el click es en el boton que corresponde al indice 0 de la lista
                if lista_botones[0].checkForInput(posicion_mouse):
                    producto_candidato = '1'
                    indice = int(producto_candidato)
                    if indice < len(productos_en_pantalla) and indice != 0:
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        producto_candidato = ""
                    
                        producto = dameProducto(lista_productos, MARGEN)
                        productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)

                    else:
                        producto_candidato = ""

                #si el click es en el boton que corresponde al indice 1 de la lista
                if lista_botones[1].checkForInput(posicion_mouse):
                    producto_candidato = '2'
                    indice = int(producto_candidato)
                    print(indice)
                    if indice < len(productos_en_pantalla) and indice != 0:
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        producto_candidato = ""
                    
                        producto = dameProducto(lista_productos, MARGEN)
                        productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)

                    else:
                        producto_candidato = ""
                
                #si el click es en el boton que corresponde al indice 2 de la lista
                if lista_botones[2].checkForInput(posicion_mouse):
                    producto_candidato = '3'
                    indice = int(producto_candidato)
                    if indice < len(productos_en_pantalla) and indice != 0:
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        producto_candidato = ""
                    
                        producto = dameProducto(lista_productos, MARGEN)
                        productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)

                    else:
                        producto_candidato = ""                    

                #si el click es en el boton que corresponde al indice 3 de la lista
                if lista_botones[3].checkForInput(posicion_mouse):
                    producto_candidato = '4'
                    indice = int(producto_candidato)
                    if indice < len(productos_en_pantalla) and indice != 0:
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        producto_candidato = ""
                    
                        producto = dameProducto(lista_productos, MARGEN)
                        productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)

                    else:
                        producto_candidato = ""                   
                
                #si el click es en el boton que corresponde al indice 4 de la lista
                if lista_botones[4].checkForInput(posicion_mouse):
                    producto_candidato = '5'
                    indice = int(producto_candidato)
                    if indice < len(productos_en_pantalla) and indice != 0:
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        producto_candidato = ""
                    
                        producto = dameProducto(lista_productos, MARGEN)
                        productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)

                    else:
                        producto_candidato = ""  

        segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

        # Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        # Dibujar de nuevo todo
        # dibujar(screen, productos_en_pantalla, producto,
        #         producto_candidato, puntos, segundos)

        # dibuja los nuevos parametros
        dibu(screen,productos_en_pantalla,producto,producto_candidato,puntos,segundos)
        lista_botones = asignar_botones(productos_en_pantalla,boton_imagen,producto)

        # actualiza cada boton asegurandose de que cada vez que el cursor pase por encima de un boton, sus letras cambien de color
        for boton in lista_botones:
            boton.changeColor(posicion_mouse)
            boton.update()
        
        pygame.display.update()  
        pygame.display.flip()

    while 1:
        # Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return


# Programa Principal ejecuta Main
if __name__ == "__main__":
    main()