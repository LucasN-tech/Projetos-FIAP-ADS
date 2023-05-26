


while True:
        #Perguntar assinatura
        while True:

            assinatura = input('Digite sua assinatura: Basic, Silver, Gold ou Platinum? ')
            if assinatura.lower() in ['basic', 'silver', 'gold', 'platinum']:
                break
            else: print('Tente novamente assinatura invalida!!')


        #Perguntar faturamento
        while True: 
            try:
                faturamento = float (input('Digite seu faturamento: '))
                break
            except ValueError:
                print('Valor invalido!!')


        #Printar o valor do bonus a ser pago
        if assinatura == 'Basic' or assinatura == 'basic':
            vlr_bonus = faturamento * (30/10)
            print(f'Valor a ser pago de acordo com a sua assinatura {assinatura}: R$ {vlr_bonus:.2f}')

        elif assinatura == 'Silver' or assinatura == 'silver':
            vlr_bonus = faturamento * (20/100)
            print(f'Valor a ser pago de acordo com a sua assinatura {assinatura}: R$ {vlr_bonus:.2f}')

        elif assinatura == 'Gold' or assinatura == 'gold':
            vlr_bonus = faturamento * (10/100)
            print(f'Valor a ser pago de acordo com a sua assinatura {assinatura}: R$ {vlr_bonus:.2f}')

        elif assinatura == 'Platinum' or assinatura == 'platinum':
            vlr_bonus = faturamento * (5/100)
            print(f'Valor a ser pago de acordo com a sua assinatura {assinatura}: R$ {vlr_bonus:.2f}')

        # encerrar o programa
        resposta = input('Deseja encerrar o programa? s/n ')
        if resposta.lower() == 's': 
            print('Programa encerrado')
            break
        else: 
            continue
    
