import turtle
turtle.hideturtle()
turtle.home()
turtle.forward(100)
turtle.left(180)
turtle.forward(200)
turtle.left(180)
turtle.home()
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(30)
turtle.right(90)

palabra = input("Defina una palabra: ")
lista = []
lista2 = []
for x in palabra:
	lista.append(x)
print(lista)
#tupla = tuple(lista)
#print(tupla)
for x in range(len(lista)):
	lista2.append("_")
#print(lista2)
#i=0
#i <= len(tupla)
"""for x in lista:

	letra = input("Digite una letra: ")

	if len(letra) != 1:
		print("Debe digitar solo una letra")
		letra = input()

	if letra == x:
		print(x)
	
	else:
		print("No coincide, elige otra letra")

	
	lista2.append(letra)
print(lista2)"""



#while n < 7:
errores = 0
for x in range(1000):
#while x < len(lista):
	letra = input("Digite una letra: ")
	n = 0
	while n < len(lista):	
		
		if letra == lista[n]:
			if lista2[n] != letra:
				#print(letra)
				#lista[n] = letra	
				lista2[n] = letra
			else:
				break

		else:
				
			
			if lista2[n] == "_":
				lista2[n] = "_"
		n += 1
	#print(lista2)
	
	#else:
	#for m in lista2:
	if letra not in lista2:
		errores += 1
		if errores == 1:
			turtle.circle(20,540)
			turtle.right(90)
		if errores == 2:
			turtle.forward(60)
			turtle.right(20)
		if errores == 3:
			turtle.forward(20)
			turtle.right(180)
			turtle.forward(20)
			turtle.right(140)
		if errores == 4:
			turtle.forward(20)
			turtle.right(180)
			turtle.forward(20)
			turtle.right(20)
			turtle.forward(40)
			turtle.left(140)
		if errores == 5:
			turtle.forward(10)
			turtle.right(180)
			turtle.forward(10)
			turtle.right(100)
		if errores == 6:
			turtle.forward(10)
			turtle.right(180)
			turtle.forward(10)
			print("Eliminado")
			break
	if lista == lista2:
		print(lista)
		print(lista2)
		print("Ganaste")
		break		
#if lista != lista2:
#	print(lista)
#	print(lista2)
#	print("Perdiste")
#else:
#	print("Perdiste")	
	

turtle.exitonclick()
print("fin del juego")