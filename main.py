
#ESTO ES UN MENSAJE DE BIENVENIDA PARA EL USUARIO

print("Bienvenidos a mi trivia de anime")
print("Pondremos a prueba tus conocimientos")

nombre=input("ingresa tu nombre: ")
#ESTAS SON LAS INSTRUCCIONES PARA JUGAR
print("Hola ",nombre,"responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta:\n")

#PREGUNTAS

print("1. ¿Cómo se llama el planeta de los sayayines?")
print("a) Namekusei")
print("b) Tierra")
print("c) Vegita") #respuesta correcta
print("d) Jupiter")

#Almacenamos la respuesta del usuario en la variable "resp_1"

resp_1=input("\n ¿Cual es tu respuesta? (Escribe la letra): ")

#SI EL USUARIO NO INGRESA LAS LETRAS A B C D, SE LE PREGUNTARÁ INFINTAS VECES HASTA QUE INGRESE LAS LETRAS CORRECTAS

while resp_1 not in ("a", "b", "c", "d"):
  resp_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")


#Evaluar la respuesta:

if resp_1=='c':
  print('\nRespuesta Correta',nombre)
  print("Toma tu loli de premio",nombre)
else:
  print('Es incorrecto, pipipi Xd\n')


print("\n2. ¿Quién es la la mejor waifu?: ")
print("a) Rem")
print("b) Kurumi") #respuesta correcta
print("c) Marin")
print("d) Jupiter")

resp_2=input("\n ¿Cual es tu respuesta? (Escribe la letra): ")

#SI EL USUARIO NO INGRESA LAS LETRAS A B C D, SE LE PREGUNTARÁ INFINTAS VECES HASTA QUE INGRESE LAS LETRAS CORRECTAS

while resp_2 not in ("a", "b", "c", "d"):
  resp_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if resp_2=='b':
  print('\nRespuesta Correta',nombre)
  print('Tome su waifu como premio Xdd')
else:
  print('Es incorrecto, pipipi Xd')

print("\n3. ¿Cómo se llama el primer pokemon de Ash? ")
print("a) Squirtle")
print("b) Charmander") 
print("c) Bulbasaur")
print("d) Pikachu") #respuesta correcta

resp_3=input("\n ¿Cual es tu respuesta? (Escribe la letra): ")

#SI EL USUARIO NO INGRESA LAS LETRAS A B C D, SE LE PREGUNTARÁ INFINTAS VECES HASTA QUE INGRESE LAS LETRAS CORRECTAS

while resp_3 not in ("a", "b", "c", "d"):
  resp_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if resp_3=='d':
  print('\nRespuesta Correta',nombre)
  print('Tome su pokemon y atrápalos a todos Xdd')
  print("\nGRACIAS POR PARTICIPAR EN MI TRIVIA",nombre)
else:
  print('ponte a estudia mejor Xd')

  



    

