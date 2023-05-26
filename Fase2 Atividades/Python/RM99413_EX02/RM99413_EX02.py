
while True:
#criar variaveis
    dias_da_semana = ['Segunda-Feira', 'Terca-feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira']
    votos_por_dia = []

#loop para input da lista 
    for dia in dias_da_semana:
        while True: 
            try:
                votos = int(input(f"Digite a quantidade de votos para {dia}, apenas numeros inteiros: "))
                break
            except ValueError:
                print('Valor invalido!!')
        votos_por_dia.append(votos)

#print do resultado 
    resultado = max(votos_por_dia)
    dia_mais_votado = dias_da_semana[votos_por_dia.index(resultado)]
    print('O dia mais votado foi:', dia_mais_votado, 'com', resultado, 'votos.')

# encerrar o programa
    resposta = input('Deseja encerrar o programa? s/n ')
    if resposta.lower() == 's': 
        print('Programa encerrado')
        break
    else: 
        continue
