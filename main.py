import random
import time
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
WHITE = '\033[37m'
MAGENTA = '\033[35m'
RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'
RESET = '\033[39m'

#Boolean
iniciar_trivia = True
intentos = 0

for numero_carga in range(5, 0, -1):
  print(numero_carga)
  time.sleep(1)
print ("Bienvenido a mi quiz sobre conejitos")
print ("Pondremos a prueba tus conocimientos")
nombre = input("Ingresa tu nombre " + CYAN + "aquí: " + RESET)
while nombre == "" or any(str.isdigit(c) for c in nombre):
  nombre = input("Solo letras, por favor.\nIntenta de nuevo:")

while iniciar_trivia == True:
  intentos += 1

  puntaje = 0
  print("Tienes", puntaje, "puntos.")
  time.sleep(2)



# Es importante dar instrucciones sobre cómo jugar:
  print ("Muy bien", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
  time.sleep(2.5)

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

# Pregunta 1
  print ("1) ¿Cuál de estos " + RED + "no " + RESET + "es un color común para un conejito?")
  print ("a) blanco")
  print ("b) marrón")
  print ("c) morado")
  print ("d) moteado")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")
  time.sleep(2)
  while respuesta_1 not in ("a", "b", "c", "d",):
      respuesta_1 = input("Por favor, responde a, b, c o d. Ingresa tu respuesta otra vez:")

  if respuesta_1 == "c":
    puntaje += random.randint(9, 21)
    print("¡Correcto! ¡Muy bien!")
    print("Tu puntaje actual es:", puntaje)
  else:
    puntaje -= random.randint(0, 11)
    print("¡Uy! Respuesta incorrecta")
    print("Tu puntaje actual es:", puntaje)

  time.sleep(2)


#Pregunta 2
  print ("\n2) ¿Cómo se les dice a los conejitos bebé?")
  print ("a) gazapo")
  print ("b) cachorro")
  print ("c) bebé, duh")
  print ("d) polluelo")
        
  respuesta_2 = input("\nTu respuesta: ")
  time.sleep(2)
  while respuesta_2 not in ("a", "b", "c", "d", "gazapo"):
      respuesta_2 = input("Por favor, responde a, b, c o d. Ingresa tu respuesta otra vez:")

  if respuesta_2 == "a":
    puntaje += 10
    print("¡Correcto! ¡Muy bien!")
    print("Tu puntaje actual es:", puntaje)

  elif respuesta_2 == "b":
    puntaje -= 10
    print("Incorrecto. Así se le dice a los bebés de otros mamíferos.")
    print("Tu puntaje actual es:", puntaje)
  elif respuesta_2 == "c":
    puntaje -= 10
    print("Incorrecto. Bebé sería el término correcto para los humanos.")
    print("Tu puntaje actual es:", puntaje)
  elif respuesta_2 == "gazapo":
    puntaje += 1000
    print("¡Increíble! Es un dato muy poco conocido sobre los conejitos.")
    print("Tu puntaje actual es:", puntaje)
  else:
    puntaje -= 10
    print("¡Uy! Respuesta incorrecta. Así se le dice a los pollitos.")
    print("Tu puntaje actual es:", puntaje)


  time.sleep(2)
  
#Pregunta 3
  print ("\n3) ¿Cuál es la mejor forma de cargar a un conejito?")
  print ("a) de las orejas")
  print ("b) sujetándolo del cuello, como un gato")
  print ("c) cargándolo como una pelota de fútbol americano")
  print ("d) sujetarlo debajo de la pancita")
  respuesta_3 = input("\nTu respuesta: ")
  while respuesta_3 not in ("a", "b", "c", "d",):
      respuesta_3 = input("Por favor, responde a, b, c o d. Ingresa tu respuesta otra vez:")

  time.sleep(2)
  if respuesta_3 == "a":
    puntaje = puntaje / 2
    print("¡Noo! Es una de las peores formas de cargar a un conejo.")
    print("Tu puntaje actual es:", puntaje)
  elif respuesta_3 == "b":
    puntaje = puntaje - 10
    print("Incorrecto. Los conejos no son gatitos. Aparte de que les duele, se pueden asfixiar.")
    print("Tu puntaje actual es:", puntaje)
  elif respuesta_3 == "c":
    puntaje = puntaje * 2
    print("¡Correcto! Esta es la mejor forma de cargar un conejito.")
    print("Tu puntaje actual es:", puntaje)
  else:
    puntaje = puntaje - 5
    print("Incorrecto. Es una de las formas, pero no es la mejor.")
    print("Tu puntaje actual es:", puntaje)

  time.sleep(2)

  
#Pregunta 4
  print ("\n4) Se " + MAGENTA + "recomienda " +  RESET + "tener la siguiente cantidad de conejitos:")
  print ("a) Solo 1")
  print ("b) En pares")
  print ("c) Tres o más")
  print ("d) Ninguno")
  respuesta_4 = input("\nTu respuesta: ")
  while respuesta_4 not in ("a", "b", "c", "d",):
      respuesta_4 = input("Por favor, responde a, b, c o d. Ingresa tu respuesta otra vez:")

  time.sleep(2)
  if respuesta_4 =="b":
    puntaje += 10
    print("¡Correcto! Lo mejor es tener conejitos en parejas.")
    print("Tu puntaje actual es:", puntaje)
  else:
    puntaje -= 10
    print("Respuesta incorrecta.")
    print("Tu puntaje actual es:", puntaje)

    
#Pregunta 5
  print ("\n5) La traducción formal de 'conejo' en inglés es:")
  print ("a) " +  GREEN + "bun" + RESET)
  print ("b) " + RED + "bunny" + RESET)
  print ("c) " + MAGENTA + "rabbit" + RESET)
  print ("d) " + CYAN +  "wabbit" + RESET)
  respuesta_5 = input("\nTu respuesta: ")
  while respuesta_5 not in ("a", "b", "c", "d",):
      respuesta_5 = input("Por favor, responde a, b, c o d. Ingresa tu respuesta otra vez:")

  time.sleep(2)
  if respuesta_5 =="c":
    puntaje +=10
    print("¡Correcto! Esta es la palabra correcta.")
    print("Tu puntaje actual es:", puntaje)
  elif respuesta_5 == "b":
    puntaje -= 10
    print("¡Respuesta incorrecta! Bunny es una forma coloquial de decir conejo, no la manera " + RED + "formal." + RESET) 
    print("Tu puntaje actual es:", puntaje)

  else:
    puntaje -= 10
    print("Respuesta incorrecta.")
    print("Tu puntaje actual es:", puntaje)

  time.sleep(2)
  print("\nCalculando resultados...")
  for numero_carga in range(random.randint(0, 9), 0, -1):
    print(numero_carga)
    time.sleep(1)




#Final
  print("\nGracias,", nombre, ",por jugar, alcanzaste", puntaje, "puntos." )
  print("\n¿Deseas jugar nuevamente?")
  repetir_trivia = input("Escribe 'si' para repetir o presiona cualquier letra para finalizar: ").lower()
  if repetir_trivia != "si":
    print("Ok,", nombre, ",espero que te hayas divertido.")
    iniciar_trivia = False
