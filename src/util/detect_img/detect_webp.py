def is_webp(caminho_arquivo):
    """
    Retorna True se o arquivo for um WEBP real.
    """
    try:
        with open(caminho_arquivo, "rb") as f:
            header = f.read(12)
            return header[:4] == b'RIFF' and header[8:12] == b'WEBP'
    except:
        return False
