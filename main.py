from miners.bitcoin import bitcoin

def main():
    print("Bem-vindo ao Script de Mineração de Criptomoedas!")
    print("Selecione a criptomoeda para mineração:")
    print("1. Bitcoin")
    # Futuras opções podem ser adicionadas aqui
    choice = input("Digite o número da opção escolhida: ")

    if choice == '1':
        print("Você selecionou Bitcoin.")
        wallet_address = input("Por favor, insira o endereço da sua carteira de Bitcoin: ")
        pool_host = "pool.supportxmr.com:3333"  # Especifique o pool host
        print("Iniciando a mineração de Bitcoin no pool " + pool_host)
        bitcoin.mine(wallet_address, pool_host)
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
