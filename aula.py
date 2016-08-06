import random
num = int(input("Quantos nomes deseja sortear?"))
lista = []

for n in range(num):
    nome = (input("Digite um nome: "))
    lista.append(nome)
    

random.shuffle(lista)
print()
print("Diante de {} nomes cadastrados o nome escolhido foi: ".format(num))

nome2 = random.choice(lista)
print()
print(nome2.upper())
