import importlib

def load_miner(coin):
    """
    Carrega dinamicamente o módulo de mineração para a criptomoeda escolhida.
    """
    try:
        miner_module = importlib.import_module(f"miners.{coin}.{coin}")
        return miner_module
    except ModuleNotFoundError:
        print(f"Módulo de mineração para {coin} não encontrado.")
        return None

def main():
    print("Bem-vindo ao script de mineração de criptomoedas!")
    coin = input("Digite o nome da criptomoeda que deseja minerar (bitcoin, ethereum, litecoin): ").lower().strip()
    
    # Carrega o módulo de mineração da criptomoeda escolhida
    miner = load_miner(coin)
    
    if miner:
        print(f"Iniciando mineração de {coin}.")
        miner.mine()
    else:
        print("Erro ao carregar o módulo de mineração.")

if __name__ == "__main__":
    main()
