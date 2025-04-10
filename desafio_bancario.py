menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[p] Poupanca
[i] Investir
[q] Sair

=> """

saldo = 0
poupanca = 0
investimentos = 0
depositado = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informar o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            depositado += valor

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "p":
        escolha = input("Deseja sacar ou depositar: ")

        if escolha = "sacar":
            saque_poupanca = float(input("Valor do saque_poupanca: ")):
            if saque_poupanca <= poupanca:
                poupanca -= saque_poupanca
                saldo += saque_poupanca
                extrato += f"Saque_poupanca: R$ {saque_poupanca:.2f}\n"
            else:
                print("O valor informado excede o valor presente na poupança.")                
            
        elif escolha = "depositar":
            deposito_poupanca = float(input("Valor do deposito_poupanca: ")):
            if deposito_poupanca <= saldo:
                saldo -= deposito_poupanca
                poupanca += deposito_poupanca
                extrato += f"Deposito_poupanca: R$ {deposito_poupanca:.2f}\n"

        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.") 
    
    elif opcao == "i":
        if saldo >= (30% depositado):
            escolha = input("Você é elegível para investir, deseja investir ou retirar: "):
            if escolha = "investir":
                investimento = float(input("Qual é o valor do investimento: ")):
                    if investimento <= saldo:
                        saldo -= investimento
                        investimentos += investimento
                        extrato += f"Investimento: R$ {investimento:.2f}\n"
                    
                    else:
                        print("O valor do investimento excede o do saldo, não foi possível realizar a operação.") 
            
            elif escolha = "retirar":
                retirada_investimento = float(input("Qual é o valor da retirada: ")):
                if retirada_investimento <= investimentos:
                    investimentos -= retirada_investimento
                    saldo += retirada_investimento
                    extrato += f"Retirada_investimento: R$ {retirada_investimento:.2f}\n"
                
                else:
                    print("O valor informado é maior do que o investido, favor escolher outro valor.")
            
            else:
                print("Opção inválida, favor escolher outra opção.")






   





    
    elif opcao == "e":
        print("\n================EXTRATO===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"\nPoupanca: R$ {poupanca:.2f}")
        print(f"\nInvestimentos: R$ {investimentos:.2f}")
        print("=========================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

