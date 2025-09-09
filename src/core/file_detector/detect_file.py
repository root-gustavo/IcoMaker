from src.util import is_jpeg, is_png, is_svg, is_webp

# Dicionário de detectores
DETECTORES = {
    "png": is_png,
    "jpeg": is_jpeg,  # cobre .jpg e .jpeg
    "webp": is_webp,
    "svg": is_svg
}

def detectar_arquivo(caminho_arquivo):
    """
    Retorna o tipo da imagem ('png', 'jpeg', 'webp', 'svg') ou None se não suportado.
    """
    for tipo, func in DETECTORES.items():
        if func(caminho_arquivo):
            return tipo
    return None
