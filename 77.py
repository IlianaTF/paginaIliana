namel = input ("ingrese el nombre de alguien al que quiera invitar a su fiesta: ")
name2 = input ("ingrese otro nombre: ")
name3 = input ("ingrese un tercer nombre: ") 
fiesta = [namel, name2, name3]
otro = input ("quieres invitar a alguien mas? (si/no): ")
while otro == "si"
    nuevo = fiesta.append (input ("ingresa otro nombre "))
    otro = input ("quieres invitar a alguien mas? (si/no): ")
print ("tienes", len (fiesta), "que van a venir a tu fiesta")
print(fiesta)
seleccion=input("ingrese uno de los nombres: ")
print(seleccion, "esta en la posicion", fiesta.index(seleccion),"en la lista")
S=input("todavia quieres que vengan? si/no")
if S=="no":
    fiesta.remove(seleccion)
print(fiesta)