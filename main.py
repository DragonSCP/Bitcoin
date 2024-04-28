import os
import sys

def load_miner(crypto):
    try:
        miner_module = __import__(f"miners.{crypto}.{crypto}", fromlist=[None])
        miner_module.mine()
    except ImportError:
        print(f"Miner for {crypto} not found.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [cryptocurrency]")
        sys.exit(1)
    
    crypto = sys.argv[1].lower()
    load_miner(crypto)

if __name__ == "__main__":
    main()
