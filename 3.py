#mostrar DESEA CONTINUAR? cuando responda (SI/NO)
mensaje=""
mensaje_invalido= True

while (mensaje_invalido == True):
    mensaje=int("ingrese mensaje:")
    mensaje_invalido = (mensaje != "si" and mensaje!= "nno")

#fin_while

print("Fin del bucle")
