from conta import ContaBancaria
from utilitarios import mostrar_menu, obter_opcao

def main():
    conta = ContaBancaria("Gabriel Bonfim")

    while True:
        mostrar_menu()
        opcao = obter_opcao()
        match opcao:
            case "1":
                conta.extrato()

            case "2":
                valor_usuario = input("Digite o valor para depósito: R$ ")
                valor = float(valor_usuario.replace(",", ".")) if "," in valor_usuario else float(valor_usuario)
                if valor > 0:
                    conta.deposito(valor)
                    print(f"Depósito de R${valor:.2f} realizado com sucesso.")
                else:
                    print("Valor inválido. Por favor, digite um valor acima de R$ 0.00")
            
            case "3":
                valor_usuario = input("Digite o valor para saque: R$ ")
                valor = float(valor_usuario.replace(",", ".")) if "," in valor_usuario else float(valor_usuario)
                if valor > 0:
                    conta.saque(valor)
                else:
                    print("Valor inválido. Por favor, insira um valor acima de R$ 0.00")

            case "4":
                break
            
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()