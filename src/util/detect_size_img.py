from PIL import Image

def obter_tamanho_imagem(caminho_arquivo):
    """
    Retorna uma tupla (largura, altura) da imagem.
    Se não for possível abrir a imagem, retorna None.
    """
    try:
        with Image.open(caminho_arquivo) as img:
            return img.width, img.height
    except Exception as e:
        print(f"Erro ao ler a imagem: {e}")
        return None
