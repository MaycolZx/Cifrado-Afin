def ExtEuclides(a,b):
  if (b==0):
    return a,1,0
  d,x1,y1 = ExtEuclides(b,a%b)
  x = y1
  y = x1 - y1 * int(a/b)
  return d,x,y

def Euclides(a,b):
  if b ==0:
    return a
  else:
    return Euclides(b,a%b)

def inverso(a,n):
  if (Euclides(a,n)==1):
    d,x,y = ExtEuclides(a,n)
    return (x%n)
  else:
    return "No tiene inverso multiplicativo."

def cifrar(a,b,cadena):
  NewChar=""
  alpha="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
  for i in cadena:
    n=0
    for j in alpha:
        if i == j:
            break
        n=n+1
    y = (a * n + b)%27
    NewChar=NewChar+alpha[y]
  return NewChar

def decifrar(a,b,cadena):
  newChar = ""
  alpha="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
  for i in cadena:
    n=0
    for j in alpha:
      if i ==j:
        break
      n=n+1
    x=(inverso(a,27)*(n-b))%27
    newChar=newChar+alpha[x]
  return newChar

#Utilizando la clave {a, b} = {4, 7}:
mjsEncrip="ELEMENTALMIQUERIDOWATSON"
msjDescif="OKHFSNKFNWFCWJHSNCHQYWFSWF"
print(f"Cifrar {mjsEncrip} es igual: {cifrar(4,7,mjsEncrip)}")
print(f"Cifrar {msjDescif} es igual: {decifrar(4,7,msjDescif)}")

mensaje = "SLBCMVRBSHZBTÑNSRQVVMSZBVHÑNBVRQVLALHZBTÑNSRQVWQAXLZWÑNAQFQV"

arreglo = []
for a in range(27):
    if (a%3 != 0):
        for b in range(27):
            print(f"[{a},{b}] = {decifrar(a,b,mensaje)}\n")
            preg = input("Desea añadirlo a la lista presione 1: ")
            if preg == "1":
                arreglo.append(decifrar(a,b,mensaje)) 
            elif (preg == " "):
                pass

print(arreglo) #Nos devuelve lo almacenado el la lista
print(f"El mensaje encriptado es : ['NOEXISTENPREGUBNTASSINRESPUBESTASOLOPREGUBNTASMALFORMUBLADAS']")

