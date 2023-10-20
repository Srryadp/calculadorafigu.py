print('             -----------Hola!!!!-----------')
print('              Bienvenid@ a nuestro programa:p')

import areas
import os 
import time

contador_cuadrado = 0 
contador_circulo = 0
contador_triangulo = 0

salir = True 


def borrarPantalla(): 
		if os.name == "posix":
   			os.system ("clear")
    		

while salir != 'salir':
	
	

	try:
		print()
		print("         Calcular Areas de fuguras Geometricas.\n")
		print("1.Cuadrado.\n2.Circulo.\n3.Triangulo")

		x=int(input("Escoja la figura: "))

		if x==1:
			
			L=int(input("Ingrese el lado: "))
			areas.area_cuadrado(L)
			contador_cuadrado += 1
			print("■")

		if x==2: 
	
			R=int(input("Ingrese el radio del circulo: "))
			areas.area_circulo(R)
			contador_circulo += 1
			print("○")

		if x==3:
	
			b=int(input("Ingrese la base: "))
			h=int(input("Ingrese la altura: "))
			areas.area_triangulo(b,h) 
			contador_triangulo += 1
			print("△")

		time.sleep(3)
		
		borrarPantalla()

		salir = input("Ingrese 'salir' para acabar con el programa o presione cualquier tecla para seguir: ")
		salir = salir.lower()

	except ValueError:
		print('ingrese un numero:)') 

print()
print('Numero de veces que fueron calculadas cada figura:', 'Cuadrado:', contador_cuadrado,'Circulo:', contador_circulo, 'Triangulo:', contador_triangulo)