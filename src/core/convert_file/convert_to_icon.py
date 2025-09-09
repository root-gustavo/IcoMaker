from PIL import Image
import os
from config.path import USER  # importa a pasta de saída do path.py
from pathlib import Path

ICONS_SIZES = [16, 32, 64, 128, 256]  # tamanhos de ícone suportados

def converter_para_ico(caminho_arquivo):
    """
    Converte uma imagem para .ico usando o tamanho mais próximo disponível.
    Salva diretamente na pasta USER definida no path.py.
    Retorna o caminho do arquivo .ico gerado.
    """
    try:
        # Garante que a pasta de saída exista
        os.makedirs(USER, exist_ok=True)

        with Image.open(caminho_arquivo) as img:
            largura, altura = img.width, img.height

            # Seleciona o tamanho de ícone mais próximo
            tamanho_proximo = min(ICONS_SIZES, key=lambda x: abs(x - max(largura, altura)))

            # Aviso se a imagem for muito grande
            if max(largura, altura) > 512:
                print("Aviso: A imagem é muito grande, pode haver distorção ao redimensionar.\n")

            # Redimensiona mantendo proporção
            img_resized = img.resize((tamanho_proximo, tamanho_proximo), Image.LANCZOS)

            # Define caminho de saída na pasta USER
            nome_arquivo = Path(caminho_arquivo).stem
            caminho_saida = USER / f"{nome_arquivo}.ico"

            # Salva como .ico
            img_resized.save(caminho_saida, format="ICO", sizes=[(tamanho_proximo, tamanho_proximo)])
            return caminho_saida

    except Exception as e:
        print(f"Erro ao converter imagem para .ico: {e}")
        return None
