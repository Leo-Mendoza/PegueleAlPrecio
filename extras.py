import random
import pygame
from pygame.locals import *
from configuracion import *

pygame.font.init()
screen = pygame.display.set_mode((ANCHO, ALTO))

fuente_principal = pygame.font.Font(pygame.font.get_default_font(), 20)
defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), 30)

class botones():
    
    #metodo __init__ inicializa el boton
    def __init__(self,image,Xpos,Ypos,text_input):
        #self.image almacena la imagen que representara al boton
        self.image = image
    
        #posicion x del boton
        self.Xpos = Xpos
        
        #posicion y del boton
        self.Ypos = Ypos
        
        #self.rect va a ser el rectangulo definido por las cordenadas x e y de self, 
        #centradas por el argumento "center" dentro de la funcion get_rect() que retorna un rectangulo
        #rectangulo donde habra colision y un efecto
        self.rect = self.image.get_rect(center=(self.Xpos,self.Ypos))
        
        #Guarda la cadena dentro del boton en la variable self.text
        self.text_input = text_input
        
        #Almacena el texto final que aparecera ya con la fuente elegida aplicada
        #Es decir, con su respectivo tamaño y color
        self.text = fuente_principal.render(self.text_input, True,'White')
        
        #Crea el rectangulo para el texto puesto que el tamaño del texto no es igual
        #Al de la imagen, por ende requiere un objeto diferente
        self.text_rect = self.text.get_rect(center=(self.Xpos,self.Ypos))

    def update(self):
        #aplica cada imagen/texto a su rectangulo
        screen.blit(self.image,self.rect)
        screen.blit(self.text,self.text_rect)
        
    def checkForInput(self,posicion):
        #como la posicion es una tupla (x,y) podemos preguntar si el cursor esta entre todo el rango de su x
        #y si su y esta en todo el rango de la y 
        if posicion[0] in range(self.rect.left,self.rect.right) and posicion[1] in range(self.rect.top,self.rect.bottom):
            return True
    def changeColor(self,posicion):
        #si el cursor esrta en este rango cambia a color azul
        if posicion[0] in range(self.rect.left,self.rect.right) and posicion[1] in range(self.rect.top,self.rect.bottom):
            self.text = fuente_principal.render(self.text_input, True,'Red')
        else: 
            #si no vuelve a su color original
            self.text = fuente_principal.render(self.text_input, True,'White')

def dameLetraApretada(key):
    if K_0 <= key and key <= K_9:
        return str(key - K_0)
    else:
        return ""


# def dibujar(screen, productos_en_pantalla, producto_principal, producto_candidato, puntos, segundos):
#     defaultFont = pygame.font.Font(pygame.font.get_default_font(), 20)
#     defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), 30)

#     # Linea del piso
#     pygame.draw.line(screen, (255, 255, 255),
#                      (0, ALTO-70), (ANCHO, ALTO-70), 5)
#     ren1 = defaultFont.render(producto_candidato, 1, COLOR_TEXTO)
#     ren2 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
#     if (segundos < 15):
#         ren3 = defaultFont.render(
#             "Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
#     else:
#         ren3 = defaultFont.render(
#             "Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
#    # Dibujar los nombres de los productos uno debajo del otro
#     x_pos = 130
#     y_pos = ALTO - (ALTO-100)

#     pos = 0
#     for producto in productos_en_pantalla:
#         nombre_en_pantalla = str(pos) + " - "+producto[0]+producto[1]
#         if producto[0] == producto_principal[0] and producto[1]== producto_principal[1]:
#             screen.blit(defaultFontGrande.render(nombre_en_pantalla,
#                         1, COLOR_TIEMPO_FINAL), (x_pos, y_pos))
#         else:
#             screen.blit(defaultFontGrande.render(
#                 nombre_en_pantalla, 1, COLOR_LETRAS), (x_pos, y_pos))
#         pos += 1
#         y_pos += ESPACIO

#     screen.blit(ren1, (190, 570))
#     screen.blit(ren2, (600, 10))
#     screen.blit(ren3, (10, 10))

def dibu(screen,productos_en_pantalla,producto_principal,producto_candidato,puntos,segundos):
    #asignamos una fuente principal
    fuente_principal = pygame.font.Font(pygame.font.get_default_font(), 20)
    #se dibuja la linea horizontal al igual que en la funcion original
    pygame.draw.line(screen, (255, 255, 255),(0, ALTO-70), (ANCHO, ALTO-70), 5)
    
    #si el producto principal es equivalente al primer producto
    #de la lista productos_en_pantalla, lo muestra 
    if producto_principal == productos_en_pantalla[0]:
        producto_principal= producto_principal[0] + ' ' + producto_principal[1]
        producto_superficie = fuente_principal.render(producto_principal,True,COLOR_TIEMPO_FINAL)
        producto_rect = producto_superficie.get_rect()
        producto_rect.center = (400,50)
    screen.blit(producto_superficie,producto_rect)
    
    #muestra los inputs del teclado 
    input_rect = fuente_principal.render(producto_candidato,True,COLOR_TEXTO)
    screen.blit(input_rect,(190, 570))
    
    #muestra el puntaje 
    score = fuente_principal.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    screen.blit(score,(600, 10))
    if (segundos < 15): 
        timer = fuente_principal.render(
            "Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        timer = fuente_principal.render(
            "Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    
    screen.blit(timer, (10, 10))
    
    # pygame.display.flip()

def asignar_botones(productos_en_pantalla,boton_imagen,producto_principal):
    if producto_principal == productos_en_pantalla[0]: 
            prod0 = productos_en_pantalla[0]
            prod1 = productos_en_pantalla[1]
            prod2 = productos_en_pantalla[2]
            prod3 = productos_en_pantalla[3]
            prod4 = productos_en_pantalla[4]
            prod5 = productos_en_pantalla[5]
    
    prod0_ = prod0[0] + ' ' + prod0[1]
    prod1_ = prod1[0] + ' ' + prod1[1]
    prod2_ = prod2[0] + ' ' + prod2[1]
    prod3_ = prod3[0] + ' ' + prod3[1]
    prod4_ = prod4[0] + ' ' + prod4[1]
    prod5_ = prod5[0] + ' ' + prod5[1]
    
    prod0 = prod0_
    prod1 = prod1_
    prod2 = prod2_
    prod3 = prod3_
    prod4 = prod4_
    prod5 = prod5_
    
    
    boton1 = botones(boton_imagen,400,160,prod1)
    boton2 = botones(boton_imagen,400,220,prod2)
    boton3 = botones(boton_imagen,400,280,prod3)
    boton4 = botones(boton_imagen,400,340,prod4)
    boton5 = botones(boton_imagen,400,400,prod5)
    
    lista_de_botones = [boton1,boton2,boton3,boton4,boton5]
    return lista_de_botones