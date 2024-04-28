import subprocess
import importlib

# Dicionário para mapear opções de criptomoedas e seus módulos correspondentes
cryptocurrencies = {
    "1": ("Bitcoin", "miners.bitcoin.bitcoin")
}

def load_module(crypto_module):
    """Função para carregar dinamicamente módulos de mineração."""
    module = importlib.import_module(crypto_module)
    return module

def main():
    print("Bem-vindo ao Script de Mineração de Criptomoedas!")
    print("Selecione a criptomoeda para mineração:")
    for key, value in cryptocurrencies.items():
        print(f"{key}. {value[0]}")
    choice = input("Digite o número da opção escolhida: ")

    if choice in cryptocurrencies:
        crypto_name, crypto_module = cryptocurrencies[choice]
        print(f"Você selecionou {crypto_name}.")
        wallet_address = input("Por favor, insira o endereço da sua carteira: ")
        pool_host = "pool.supportxmr.com:3333"  # Especifique o pool host aqui ou peça ao usuário
        print(f"Iniciando a mineração de {crypto_name} no pool {pool_host}...")
        mining_module = load_module(crypto_module)
        mining_module.mine(wallet_address, pool_host)
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
