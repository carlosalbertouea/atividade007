import sys

log_file = 'log.txt'
log_lines = [] #lista para armazenar todas as linhas lidas

#mapeamento de meses
month_map = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

#função chave da a ordenação
def get_sort_key(log_line):
    """Extrai (Mês_Num, Dia_Num, Hora_Str) de uma linha de log para ordenação."""
    try:
        fields = log_line.split()
        if len(fields) < 3:
             #se linha mal formatada, colocar no final
             return (99, 99, "99:99:99")

        month_str = fields[0]
        day_str = fields[1]
        time_str = fields[2] #formato HH:MM:SS

        month_num = month_map.get(month_str, 0) #obtem número do mês, 0 se não encontrar
        day_num = int(day_str) #converte dia para inteiro

        return (month_num, day_num, time_str)
    except (IndexError, ValueError):
        #se falhar a conversão ou acesso ao índice, trata como mal formatada
        #coloca estas linhas no final da ordenação
        return (99, 99, "99:99:99")

try:
    with open(log_file, 'r') as f:
        #lê as linhas, remove espaços extras e ignora linhas vazias
        log_lines = [line.strip() for line in f if line.strip()]

except FileNotFoundError:
    print(f"Erro: Arquivo '{log_file}' não encontrado.", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}", file=sys.stderr)
    sys.exit(1)

print("--- Logs Ordenados por Horário  ---")
if log_lines:
    #ordena a lista de linhas usando a função chave definida acima
    sorted_log_lines = sorted(log_lines, key=get_sort_key)

    # imprime as linhas ordenadas
    for line in sorted_log_lines:
        print(line)
else:
     print("Nenhuma linha de log encontrada ou lida.")
