import pygame
pygame.init()

pantalla_altura = 500
pantalla_anchura = 600
pantalla = pygame.display.set_mode((pantalla_anchura,pantalla_altura))

pygame.display.set_caption('GUI demo')

icono = pygame.image.load(("imagenes\green-pixel-dollar-symbol.png"))
pygame.display.set_icon(icono)

fuentePrincipal = pygame.font.SysFont('haettenschweiler',30)

color1 = (255,51,56)
color2 = (255,138,16)
color3 = (255,208,74)
color4 = (255,255,151)
color5 = (255,255,214)



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
        self.text = fuentePrincipal.render(self.text_input, True,'White')
        
        #Crea el rectangulo para el texto puesto que el tamaño del texto no es igual
        #Al de la imagen, por ende requiere un objeto diferente
        self.text_rect = self.text.get_rect(center=(self.Xpos,self.Ypos))
    
    def update(self):
        #aplica cada imagen/texto a su rectangulo
        pantalla.blit(self.image,self.rect)
        pantalla.blit(self.text,self.text_rect)
        
    def checkForInput(self,posicion):
        #como la posicion es una tupla (x,y) podemos preguntar si el cursor esta entre todo el rango de su x
        #y si su y esta en todo el rango de la y 
        if posicion[0] in range(self.rect.left,self.rect.right) and posicion[1] in range(self.rect.top,self.rect.bottom):
            print('Boton apretado')
    def changeColor(self,posicion):
        #si el cursor esrta en este rango cambia a color azul
        if posicion[0] in range(self.rect.left,self.rect.right) and posicion[1] in range(self.rect.top,self.rect.bottom):
            self.text = fuentePrincipal.render(self.text_input, True,'Blue')
        else: 
            #si no vuelve a su color original
            self.text = fuentePrincipal.render(self.text_input, True,'White')
            
#Cargo la imagen para el boton y la escalo a un tamaño apropiado  
boton_imagen = pygame.image.load("imagenes\start_button.png")
boton_imagen = pygame.transform.scale(boton_imagen, (150,80))
#llamo a la clase y la guardo en una variable
boton = botones(boton_imagen,300,250,'ON')     
        
#bucle del juego

run = True
while run:
    
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            boton.checkForInput(pygame.mouse.get_pos())

    pantalla.fill(color5) 
    boton.update()
    boton.changeColor(pygame.mouse.get_pos())
    pygame.display.update()   


