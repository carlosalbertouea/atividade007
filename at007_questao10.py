import sys
from collections import Counter

log_file = 'log.txt'
ssh_ips = [] #lista para guardar os ips das conexões ssh

try:
    with open(log_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue #pula linhas vazias

            fields = line.split()

            #verifica se é uma linha de log do sshd e se tem campos suficientes para o ip
            if len(fields) >= 11 and "sshd[" in fields[4]:
                if fields[7] == "from": #para Accepted password
                   ip_address = fields[8]
                   ssh_ips.append(ip_address)
                elif fields[9] == "from": #para Failed password
                    ip_address = fields[10]
                    ssh_ips.append(ip_address)

except FileNotFoundError:
    print(f"erro: arquivo '{log_file}' não encontrado.", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"ocorreu um erro inesperado ao processar o arquivo: {e}", file=sys.stderr)
    sys.exit(1)

#conta a frequência de cada ip
ip_counts = Counter(ssh_ips)

#imprime os resultados ordenados pela contagem, do maior para o menor
print("--- Contagem de conexões SSH por IP (Maior para Menor) ---")
if ip_counts:
    for ip, count in ip_counts.most_common():
        print(f"{count:>7} {ip}") #alinha a contagem à direita
else:
    print("nenhuma conexão ssh encontrada no log.")
