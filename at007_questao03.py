Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
... 
... def listar_ips_ssh():
...     try:
...         with open('log.txt', 'r') as arquivo:
...             for linha in arquivo:
...                 if 'sshd' in linha and 'from' in linha:
...                     # Expressão regular para encontrar o IP após a palavra 'from'
...                     match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', linha)
...                     if match:
...                         print(match.group(1))
...     except FileNotFoundError:
...         print('Arquivo não encontrado. Verifique o caminho.')
... 
... if __name__ == "__main__":
