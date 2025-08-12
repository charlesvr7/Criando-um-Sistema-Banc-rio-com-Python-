'''
1) Todos depositos armazenados em uma unica variavel e exibidos na operacao de extrato
2) O sistema permite apenas 3 saques diários
3) O limite diário de saque é de R$ 500,00;
4) o sistema deve exibir mensaem de erro quando o usuário tentar sacar um valor maior que o saldo disponível
5) essa operacao deve listar todas as operações realizadas na conta "extrato", informando o saldo atual;
6) sE USUARIO NAO TEM SALDO, apareca uma mensagem "Saldo insuficiente para saque"
6) Se o extrato estiver em branco exibir a mensagem "Não foram realizadas movimentações".
Os valores tem que serem exibidos com 2 casas decimais.
'''


menu = """
############### Menu ###############
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
####################################
"""
saldo = 0
limite = 500
extrato = ""    
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito:  \n"))
        if valor >0:
            saldo += valor
            extrato += f"Foram depositados: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.\n")
    elif opcao == 's':
        valor = float(input(f"Digite o valor de Saque: \n"))
        excedeu_saldo= valor >saldo
        valor_limite = valor > limite
        excedeu_saque = numero_saques>=LIMITE_SAQUES

        if excedeu_saldo:
            print('Saldo Insuficiente')
        elif excedeu_saque:
            print('Voce excedeu o numero de saques')
        elif valor_limite:
            print('Voce excedeu o limite diário de saques')
        elif valor > 0:
            saldo -= valor
            extrato += f"foram sacados: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")         

    elif opcao == 'e':
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == 'q':
        print("Obrigado por utilizar nossos serviços!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")