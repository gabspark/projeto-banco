# utils.py

def mostrar_menu():
    menu = "Menu"
    print_menu = menu.center(20)
    print(print_menu)

    print("""
        1. Extrato
        2. Depósito
        3. Saque
        4. Sair 
        """)
    
def obter_opcao():
    return input("Escolha uma opção: ")