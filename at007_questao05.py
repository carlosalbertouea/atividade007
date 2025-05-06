Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def contar_logins():
...     sucesso = 0
...     falha = 0
...     try:
...         with open('log.txt', 'r') as arquivo:
...             for linha in arquivo:
...                 if 'Accepted password' in linha:
...                     sucesso += 1
...                 elif 'Failed password' in linha:
...                     falha += 1
...         print(f'Total de logins bem-sucedidos: {sucesso}')
...         print(f'Total de falhas de login: {falha}')
...     except FileNotFoundError:
...         print('Arquivo não encontrado. Verifique o caminho.')
... 
... if __name__ == "__main__":
        contar_logins()
