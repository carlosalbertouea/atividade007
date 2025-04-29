import sys
from collections import Counter #para contar  as falhas por usuário

log_file = 'log.txt'
failed_login_users = [] #guarda os nomes de usuário das tentativas falhas

try:
    with open(log_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue #pula linhas vazias

            fields = line.split()

            #procura por linhas de falha de senha e garante que há campos suficientes
            if len(fields) >= 9 and fields[5] == "Failed" and fields[6] == "password":
                username = fields[8]
                failed_login_users.append(username)

except FileNotFoundError:
    print(f"erro: arquivo '{log_file}' não encontrado.", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"ocorreu um erro inesperado ao processar o arquivo: {e}", file=sys.stderr)
    sys.exit(1)

#frequência de cada usuário na lista de falhas
user_fail_counts = Counter(failed_login_users)

#imprime os usuários com mais de uma falha
print("--- Usuários com mais de uma falha de login  ---")
found_users = False

for user, count in user_fail_counts.items():
    if count > 1:
        print(user)
        found_users = True

if not found_users:
    print("nenhum usuário encontrado com mais de uma falha de login.")
