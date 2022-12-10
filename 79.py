nums = []
cont = 0
while cont <3:
    num = int (input ("ingresa un numero: "))
    nums.append (num)
    print (nums)
    cont = cont + 1
ultimoN = input ("quieres que l ultimo numero se guarde? si/no: ")
if ultimoN == "no":
    nums.remove (num)
print (nums)