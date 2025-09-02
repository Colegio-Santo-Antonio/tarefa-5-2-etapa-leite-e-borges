numero=input()
impares=[ ]
for i in numero[-1::-2]:
    impares.append(int(i))
pares = []
for i in numero[-2::-2]:
  if 2*int(i)<10:
    pares.append(2*int(i))
  else:
    pares.append(2*int(i)-10+1)
 soma = sum(impares)+sum(pares)
 if int(soma/10) == soma/10:
   print("cartão válido")
 else:
   print("cartão inválido")
