import pygame
pygame.init()
pantalla_altura = 500
pantalla_anchura = 300
pantalla = pygame.display.set_mode((pantalla_altura,pantalla_anchura))
pygame.display.set_caption('GUI demo')

icono = pygame.image.load(("imagenes\green-pixel-dollar-symbol.png"))
pygame.display.set_icon(icono)

boton =[pygame.image.load("imagenes\start_button.png"),
       pygame.image.load("imagenes\pushed_button.png")]

class botones():
    def __init__(selF,imagen,posicion,text_input,fuente,color_base,color_apuntado):
        selF.imagen = imagen
        selF.x_posicion =posicion[0]
        selF.y_posicion =posicion[1]
        selF.fuente = fuente
        selF.color_base, selF.color_apuntado = color_base,color_apuntado
        selF.text_input = text_input
        selF.texto =selF.fuente.render(selF.text_input,True,selF.color_base)
        if selF.image == None:
            selF.imagen = selF.fuente
        selF.rect = selF.imagen.get_rect(center=(selF.x_posicion,selF.y_posicion))
        selF.texto_rect = selF.texto.get_rect(center=(selF.x_posicion,selF.y_posicion))
       
    def actualizacion(selF,pantalla):
        if selF  is not None:
            pantalla.blit(selF.imagen,selF.rect)
        pantalla.blit(selF.texto,selF.rect)
    
    
        

#bucle del juego
def bucle():
    run = True
    while run:
        pantalla.fill((234,182,118))
        pygame.display.update() 
        
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                run = False
         
    pygame.quit()   


print(bucle())
