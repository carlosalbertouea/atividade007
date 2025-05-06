Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def contar_linhas():
...     try:
...         with open('log.txt', 'r') as arquivo:
...             linhas = arquivo.readlines()
...             print(f'Total de linhas no log: {len(linhas)}')
...     except FileNotFoundError:
...         print('Arquivo não encontrado. Verifique o caminho.')
... 
... if __name__ == "__main__":
        contar_linhas()
