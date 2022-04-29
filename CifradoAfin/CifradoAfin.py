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
  cadena2=""
  abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
  for i in cadena:
    n=0
    for j in abc:
        if i == j:
            break
        n=n+1
    y = (a * n + b)%27
    cadena2=cadena2+abc[y]
  return cadena2

def decifrar(a,b,cadena):
  cadena2 = ""
  abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
  for i in cadena:
    n=0
    for j in abc:
      if i ==j:
        break
      n=n+1
    x=(inverso(a,27)*(n-b))%27
    cadena2=cadena2+abc[x]
  return cadena2

dr="ELEMENTALMIQUERIDOWATSON"
fr="OKHFSNKFNWFCWJHSNCHQYWFSWF"

print(f"Cifrar {dr} es igual: {cifrar(4,7,dr)}")
print(f"Cifrar {fr} es igual: {decifrar(4,7,fr)}")

