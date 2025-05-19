import time
import random
print("\t\n\n-=-=- Bem-vindo ao Sorteio Online! -=-=-\n\n")
nomes = []
sair = 0
while sair <= 9:
    name = input("Nome: ")
    nomes.append(name)
    sair += 1
# Embaralha os nomes para sorteio
random.shuffle(nomes)
numeros_sort = []
print("\n\n\nSorteando...")
for x in range(3):
    time.sleep(0.8)
    print(x," ...")
time.sleep(0.5)
print("\n\n\n\n\tNome do Líder e Número do Mandamento:")
for nome in nomes:
    while True:
        numero = random.randint(1, 10)
        if numero not in numeros_sort:
            numeros_sort.append(numero)
            print(nome, " -->", numero)
            time.sleep(0.2)
            break
