tv = ["Bob Esponja", "Rugrats", "Peppa Pig", "Pequeños Traviesos"]
for i in tv:
    print (i)
print ()
Ntv = input ("ingresa otro tv show: ")
position = int (input ("escribe un numero entre 0-3: "))
tv.insert (position, Ntv) 
for i in tv:
    sprint (i)