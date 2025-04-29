import sys

log_file = 'log.txt'
sudo_users = set() #armazena users únicos

try:
    with open(log_file, 'r') as f:
        for line in f:
            line = line.strip() #remove espaços de linha
            if not line:
                continue #pula linhas em branco

            fields = line.split()

            #verificar se a linha é de log do sudo e se tem campos suficientes
            if len(fields) >= 6 and "sudo[" in fields[4]:
                 username = fields[5]
                 sudo_users.add(username)

except FileNotFoundError:
    print(f"Erro: Arquivo '{log_file}' não encontrado.", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Ocorreu um erro inesperado ao processar o arquivo: {e}", file=sys.stderr)
    sys.exit(1) 

print("--- Usuários que executaram comandos com sudo  ---")
if sudo_users:
    #conversao do  set para lista para poder ordenar
    sorted_users = sorted(list(sudo_users))
    for user in sorted_users:
        print(user)
else:
    print("Nenhum usuário utilizando 'sudo' foi encontrado.")
