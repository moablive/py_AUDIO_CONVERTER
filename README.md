# Gerenciador de Áudio - Conversor para 44.1 kHz

## Descrição
Este projeto é um gerenciador de áudio desenvolvido em Python que permite importar arquivos WAV de 24 ou 32 bits e convertê-los para 44.1 kHz. Ele inclui uma interface gráfica para facilitar a seleção e conversão dos arquivos.

## Funcionalidades
- Importar arquivos WAV
- Selecionar profundidade de bits (24 ou 32 bits)
- Converter arquivos para 44.1 kHz
- Salvar os arquivos convertidos em uma pasta específica

## Tecnologias Utilizadas
- Python 3.x
- tkinter - Interface gráfica
- pydub - Processamento de áudio
- mutagen - Manipulação de metadados de áudio
- ffmpeg - Requisito para manipulação de arquivos WAV

## Instalação

1. Clone o repositório:
   git clone https://github.com/seu-usuario/py_AUDIO_CONVERTER.git
   cd py_AUDIO_CONVERTER

2. Instale as dependências:
   pip install -r requirements.txt

3. Instale o ffmpeg se ainda não tiver:
   pip install ffmpeg-python
   Ou baixe manualmente de FFmpeg.org (https://ffmpeg.org/download.html) e adicione ao PATH.

## Como Usar

1. Execute o script principal:
   python converter.py

2. Na interface gráfica:
   - Clique em "Importar Arquivos WAV" para selecionar os arquivos.
   - Escolha a profundidade de bits (24 ou 32 bits).
   - Clique em "Converter para 44.1 kHz" para iniciar a conversão.

3. Os arquivos convertidos serão salvos na pasta output/.

## Exemplo de Uso
from converter import converter_para_44100
converter_para_44100("meu_arquivo.wav")

## Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para contribuir!
