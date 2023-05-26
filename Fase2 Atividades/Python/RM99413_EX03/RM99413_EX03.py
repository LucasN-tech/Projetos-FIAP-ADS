#coment teste

notas_impares = []
notas_pares = []

for i in range(1, 51, 2):
    print('Voce esta digitando a nota dos alunos impares')
    nota = float(input(f"Por favor,Insira a nota do aluno de numero {i}: "))
    notas_impares.append(nota)

for i in range(2, 51, 2):
    print('Voce esta digitando a nota dos alunos pares')
    nota = float(input(f"Por favor, Insira a nota do aluno de numero {i}: "))
    notas_pares.append(nota)

media_impares = sum(notas_impares) / len(notas_impares)
media_pares = sum(notas_pares) / len(notas_pares)

print(f'A media dos alunos impares foi de {media_impares}')
print(f'A media dos alunos pares foi de {media_pares}')

if media_impares > media_pares:
    print("A metade dos alunos impares teve a maior media.")
elif media_pares > media_impares:
    print("A metade dos alunos pares teve a maior media.")
else:
    print("As duas metades tiveram a mesma media.")
