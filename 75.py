num = [452, 789,264, 215]
for i in num:
    print (i)
seleccion = int (input ("Enter a number from the list: "))
if seleccion in num:
    print (seleccion, "esta en posicion", num.index (seleccion)) 
else:
    print ("no esta en la lista")