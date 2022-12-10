materias=["ingles","historia","fisica","quimica","biologia","literatura"]
print(materias)
N=input("cual de estas materias no te gusta?")
r=materias.index(N)
del materias[r]
print(materias)