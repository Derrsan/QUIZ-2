N = int(input(""))
Contador = 0
ContadorDentro = 0
ContadorFuera = 0
while (Contador<N):
    X = int(input(""))
    Contador = Contador+1
    if (10<=X<=20):
        ContadorDentro = ContadorDentro + 1

    if (10>X or X>20):
        ContadorFuera = ContadorFuera + 1

print(f"{ContadorDentro} in")
print(f"{ContadorFuera} out")