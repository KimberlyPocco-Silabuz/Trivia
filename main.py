#puntuacion inicial
import random  
puntaje = random.randint(1, 10)
aciertos=0
preguntasTotales=4
#bienvenida
print("\033[36m****************************************\033[39m")
print ("\033[35mBIENVENIDO A MI TRIVIA SOBRE COMPUTACIÓN\033[39m")
print("\033[36m****************************************\033[39m")
print ("Pondremos a prueba tus conocimientos")
print("Te ayudaremos con un puntaje inicial ")
print ("Comenzarás con", puntaje, "puntos")
print("Que comience el juego...")


print("\033[36m****************************************\033[39m")
nombre = input ("\033[34m\nIngresa tu nombre: \033[39m")

#instrucciones
print ("\nHola \033[31m",nombre, "\033[39mresponde las siguientes preguntas escribiendo la letra de la alternativa y presionando \033[31m'Enter'\033[39m para enviar tu respuesta:\n")

# Pregunta 1
print ("\033[33m1) ¿Quién fue el enemigo de Sherlock Holmes?")
print ("a) John H. Watson")
print ("b) James Moriarty")
print ("c) Inspector Lestrade")
print ("d) Irene Adler\033[39m")
#b)James Moriarty
# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")

while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_1 == "b":
  puntaje += 10
  aciertos+=1
  print ("Muy bien", nombre, "!")
  
else:
  puntaje = puntaje -1
  print ("Incorrecto, se te descontará 1 punto", nombre, "!")


print(nombre, "llevas", puntaje, "puntos")

# Pregunta 2
print ("\n\033[33m2) ¿El ´ingenio sin medida es el mayor tesoro del hombre´ es el lema de qué casa?")
print ("a) Gryffindor")
print ("b) Hufflepuff")
print ("c) Ravenclaw")
print ("d) Slytherin\033[39m")
#c)ravenclau
# Almacenamos la respuesta del usuario en la variable "respuesta_2"
respuesta_2 = input("\nTu respuesta: ")

while respuesta_2 not in ("a", "b", "c", "d"):
  respuesta_2 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_2 == "c":
  puntaje += 10
  aciertos+=1
  print ("Correcto", nombre, "!")
else:
  puntaje = puntaje -1
  print ("Incorrecto, se te descontará 1 punto", nombre,"!")

print(nombre, "llevas", puntaje, "puntos")

# Pregunta 3
print ("\n\033[33m3) ¿Cómo se llama la amada del protagonista en el libro el ´El conde de montecristo´?")
print ("a) Mercedes Herrera")
print ("b) Herminie Danglars")
print ("c) Beatriz Villefort")
print ("d) Julie Herbault\033[39m")
#a)Mercedes Herrera
# Almacenamos la respuesta del usuario en la variable "respuesta_3"
respuesta_3 = input("\nTu respuesta: ")

while respuesta_3 not in ("a", "b", "c", "d"):
  respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

# Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
if respuesta_3 == "a":
  puntaje += 10
  aciertos+=1
  print ("Correcto", nombre, "!")
else:
  puntaje = puntaje -1
  print ("Incorrecto, se te descontará 1 punto", nombre, "!")

print(nombre, "llevas", puntaje, "puntos")


# Pregunta 4
print ("\n\033[33m4) ¿Cuál de estos NO es el nombre de una de las hermanas del libro ´Mujercitas´de Louisa May Alcott?")
print ("a) Jo")
print ("b) Meg")
print ("c) Kate")
print ("d) Beth\033[39m")
#c)kate
# Almacenamos la respuesta del usuario en la variable "respuesta_4"
respuesta_4 = input("\nTu respuesta: ")

while respuesta_4 not in ("a", "b", "c", "d"):
  respuesta_4 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_4 == "a":
  print ("Incorrecto, Jo es una de las hermanas! ...")
  puntaje = puntaje -5
elif respuesta_4 == "b":
  print ("Incorrecto Meg es la hermana mayor...")
  puntaje = puntaje /2
elif respuesta_4 == "d":
  print ("Incorrecto Beth es una de las hermanas! ...")
  puntaje = puntaje +1/2
else:
  print ("Correcto! ...\n")
  aciertos+=1
  puntaje = puntaje * 2


print ("\n\033[34mGracias\033[39m"+"\033[33m", nombre,"\033[39m" +"\033[34mpor jugar mi trivia, alcanzaste\033[39m"+"\033[31m", puntaje, "puntos\033[39m"+ " Tienes ", aciertos," aciertos de",preguntasTotales)