#Esta funcion busca la letra en list_word y retorna la posicion
def search(vec,letter):
  for i in range(0,len(vec)):
    if vec[i]==guess:
      return i
  return -1

#Ahorcado
word="avion"
list_word=list(word)
list_guess=["_"]*len(word)
tries=6
cont=0 
print(len(word))#contador de correctas para salir en caso de que gane
while tries>0:
  print(f"Tienes {tries} intentos")
  print(list_guess)
  guess=input("Adivina una letra: ")
  if guess in word:
    print("Correcto")
    pos=search(list_word,guess)
    list_guess[pos]=guess
    cont+=1
  else:
    print("Incorrecto")
    tries=tries-1
  #condiciones del break  
  if cont==len(word):
    print("Victoria!!")
    flag=True
    break
  elif tries==0:
    print("Derrota :c")
    