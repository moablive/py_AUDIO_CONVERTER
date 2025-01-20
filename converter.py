import os
from pathlib import Path
from mutagen.mp3 import MP3
from pydub import AudioSegment
import tkinter as tk
from tkinter import filedialog, messagebox

class AudioConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Áudio para 44.1 kHz")
        self.root.iconbitmap("D:/!Developer/py_AUDIO_CONVERTER/ico.ico")
        self.root.geometry("350x150")

        self.label = tk.Label(root, text="Selecione arquivos WAV para conversão")
        self.label.pack()
        
        self.btn_import = tk.Button(root, text="Importar Arquivos WAV", command=self.importar_arquivos)
        self.btn_import.pack()
        
        self.bit_depth_var = tk.StringVar(value="24 bits")
        self.radio_24 = tk.Radiobutton(root, text="WAV 24 bits", variable=self.bit_depth_var, value="24 bits")
        self.radio_24.pack()
        
        self.radio_32 = tk.Radiobutton(root, text="WAV 32 bits", variable=self.bit_depth_var, value="32 bits")
        self.radio_32.pack()
        
        self.btn_converter = tk.Button(root, text="Converter para 44.1 kHz", command=self.converter_arquivos)
        self.btn_converter.pack()
        
        self.arquivos = []
    
    def importar_arquivos(self):
        arquivos = filedialog.askopenfilenames(filetypes=[("Arquivos WAV", "*.wav")])
        if arquivos:
            self.arquivos = arquivos
            messagebox.showinfo("Sucesso", f"{len(arquivos)} arquivos importados com sucesso!")
    
    def converter_arquivos(self):
        if not self.arquivos:
            messagebox.showwarning("Atenção", "Nenhum arquivo selecionado!")
            return
        
        for arquivo in self.arquivos:
            converter_para_44100(arquivo)
        
        messagebox.showinfo("Concluído", "Todos os arquivos foram convertidos para 44.1 kHz!")

def converter_para_44100(caminho_arquivo, pasta_destino="output"):
    """Converte arquivos WAV 24/32 bits para 44.1 kHz."""
    try:
        audio = AudioSegment.from_file(caminho_arquivo)
        audio = audio.set_frame_rate(44100)
        output_path = Path(pasta_destino) / Path(caminho_arquivo).name
        audio.export(output_path, format="wav")
        print(f"Convertido: {output_path}")
    except Exception as e:
        print(f"Erro na conversão: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioConverterApp(root)
    root.mainloop()
