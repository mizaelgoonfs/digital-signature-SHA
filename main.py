from utility_functions import generateKey, digitalSigner, verifyDigitalSign

def switch():
    print("\nMENU: \n")
    print("1 - Gerar par de chaves e seus respectivos arquivos (.pem);")
    print("2 - Assinar um arquivo texto;")
    print("3 - Verificar assinatura;")
    print("0 - Sair.\n")

    option = input("Digite o número correspondente à opção: ")

    if option == "0":
        print("Saindo...")
        return 0
    elif option == "1":
        generateKey()
        return 1
    elif option == "2":
        digitalSigner()
        return 2
    elif option == "3":
        verifyDigitalSign()
        return 3
    else:
        print("Opção inválida!")
        return 4

if __name__ == "__main__":
    option = switch()
    while(option != 0):
         option = switch()