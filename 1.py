#Ingrese el color (1=Blanco, 2=Negro)
color=""/0
color_invalido= True

while (color_invalido == True):
    color=int("ingrese 1/2:")
    color_invalido = (color!= 1 or color!= 2)

#fin_while

print("Fin del bucle")
