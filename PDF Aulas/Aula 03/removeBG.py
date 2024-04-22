from rembg import remove
from PIL import Image
import os

caminho = "C:/Users/bisto/OneDrive/Documentos/GitHub/Mathefian-Estudo-Criacao-de-jogos/Modelo de personagem não trabalhados/Personagem Principal/Blender/"
nomeImage = "albedo.png"
formato = ".png"
listacaminhos = ['Andando Frente', 'Ataque Costas', 'Ataque Frente', 'Ataque Lado', 
                 'Correndo Costa', 'Correndo Frente', 'Correndo Lado', 'Flutuando Costas', 'Flutuando Frente', 'Flutuando Lado', 
                 'Idle Costas', 'Idle Frente', 'Idle Lado', 'Nadando Costa', 'Nadando Frente', 'Nadando Lado', 
                 'Pulando Costa', 'Pulando Frente', 'Pulando Lado']
k = 0
for i in listacaminhos:
    caminhototal = f"{caminho}/{i}"
    total = len(os.listdir(caminhototal))
    k+=1
    for i in range(total):
        id = i+1
        caminhoimagem = f"{caminhototal}/{nomeImage}{id:04d}{formato}"
        imgemarq = Image.open(caminhoimagem)
        imagesembg = remove(imgemarq)
        imagesembg.save(f"{caminhototal}/{nomeImage}{id:04d}{formato}")
        print(f"Progresso: {id}/{total} - {caminhoimagem}")
    print(f"Finalizado: {caminhototal} {k}/{len(listacaminhos)}")
