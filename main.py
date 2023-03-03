import json
import subprocess
from datetime import timedelta


def run_test():
    print('Consultando a velocidade do seu link...')
    prompt_command = 'speedtest-cli --json > teste.json'
    test = subprocess.run(prompt_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if test.returncode == 1:
        raise BaseException('Sem conexão')


tamanho_arquivo = float(input('Tamanho(em MB): ')) * 8

try:
    run_test()
except BaseException as ex:
    print(ex)
    exit(0)

with open('./teste.json', 'r') as arquivo:
    conteudo = arquivo.read()

dados = json.loads(conteudo)

download = dados['download'] / 1_000_000
upload = dados['upload'] / 1_000_000
download_MB = download / 8
upload_MB = upload / 8

print(f'\nDownload {download_MB:.2f} MB/s\n'
      f'Upload: {upload_MB:.2f} MB/s')

tempo_download = (tamanho_arquivo / download_MB) / 60
tempo_upload = (tamanho_arquivo / upload_MB) / 60

horas_download = str(timedelta(minutes=int(tempo_download)))
horas_download_formatadas = horas_download[-8:]
horas_upload = str(timedelta(minutes=int(tempo_upload)))
horas_upload_formatadas = horas_download[-8:]

print(f'Tempo estimado para download: {horas_download_formatadas} ')
print(f'Tempo estimado para upload: {horas_upload_formatadas} ')
