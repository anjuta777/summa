def countnumbers(teksts):
  summa = 0
  for simbols in teksts:
    summa = summa + int(simbols)
  return summa
teksts = input("Ievadi skaitli")
rez = countnumbers(teksts)
print (rez)