import subprocess

def mine(wallet_address, pool_host='pool.supportxmr.com:3333'):
    # Comando para iniciar o minerador xmrig
    command = [
        './xmrig',
        '-o', pool_host,           # Pool de mineração
        '-u', wallet_address,      # Endereço da carteira
        '-p', 'x',                 # Senha do pool, se necessário
        '--donate-level', '1',     # Nível de doação para o desenvolvedor do xmrig (1% é o mínimo)
        '--threads', '4',          # Número de threads do CPU a utilizar
        '--cpu-priority', '5'      # Prioridade do processo CPU (valor entre 0 e 5)
    ]
    # Executa o comando em subprocesso. Adapte o caminho conforme necessário para seu sistema.
    subprocess.run(command, cwd='/path/to/xmrig/build')
