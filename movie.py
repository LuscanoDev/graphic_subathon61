import os
from moviepy.editor import ImageSequenceClip
import re

# Define o caminho para a pasta de imagens
image_folder = 'images'

# Função para extrair o número da imagem a partir do nome do arquivo
def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else -1

# Coleta e ordena as imagens com base no número extraído
images = sorted([os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(".png")],
                key=lambda x: extract_number(x))

# Cria o vídeo a partir das imagens
clip = ImageSequenceClip(images, fps=30)

# Salva o vídeo como 'output_video.mp4'
clip.write_videofile('output_video.mp4', codec='libx264')
