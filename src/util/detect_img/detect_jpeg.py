import os

def is_jpeg(caminho_arquivo):
    """
    Retorna True se o arquivo for um JPEG real (.jpg ou .jpeg) e verificar o cabeçalho.
    """
    # Verifica extensão
    if not caminho_arquivo.lower().endswith((".jpg", ".jpeg")):
        return False

    # Verifica cabeçalho e footer
    try:
        with open(caminho_arquivo, "rb") as f:
            header = f.read(2)
            f.seek(-2, os.SEEK_END)
            footer = f.read(2)
            return header == b'\xff\xd8' and footer == b'\xff\xd9'
    except:
        return False
