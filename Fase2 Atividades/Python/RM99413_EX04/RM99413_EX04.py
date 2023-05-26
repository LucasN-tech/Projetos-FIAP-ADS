

comentario1 = ('Pedir ao usuário que digite os minutos atuais', encoding = "UTF-8")
print(comentario1)

minutos = int(input("Digite os minutos atuais: "))
# Calcular o fatorial dos minutos
fatorial = 1
for i in range(1, minutos+1):
    fatorial *= i
# Criar a senha e exibir na tela
senha = "LIBERDADE" + str(fatorial)
print(f"Senha: {senha}")

