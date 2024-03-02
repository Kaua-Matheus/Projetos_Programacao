import subprocess

# netsh wlan show profiles
# netsh wlan show profile "internet_exemplo" key = clear

nome_wifi = "internet_exemplo"
informacoes = subprocess.check_output(["netsh", "wlan", "show", "profile", nome_wifi, "key", "=", "clear"], encoding="cp858")

for linha in (informacoes.split('\n')):
    if "Conteúdo da Chave" in linha:
        pos = linha.find(":")
        senha = linha[pos + 2:]
        print(senha)
