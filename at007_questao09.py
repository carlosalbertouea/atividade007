import sys

log_file = 'log.txt'

print("--- Comandos executados via sudo  ---")

try:
    with open(log_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue #pula linhas vazias

            #verifica se a linha contém uma entrada de sudo e a palavra COMMAND=
            if "sudo[" in line and "COMMAND=" in line:
                #encontra a posição inicial do comando (seguro devido ao check 'COMMAND=' acima)
                command_start_index = line.index("COMMAND=") + len("COMMAND=")
                #extrai o comando do resto da linha
                command = line[command_start_index:]
                print(command)

except FileNotFoundError:
    print(f"erro: arquivo '{log_file}' não encontrado.", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"ocorreu um erro inesperado ao processar o arquivo: {e}", file=sys.stderr)
    sys.exit(1)
