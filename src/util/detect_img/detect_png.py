def is_png(caminho_arquivo):
    """
    Retorna True se o arquivo for um PNG real.
    """
    try:
        with open(caminho_arquivo, "rb") as f:
            header = f.read(8)
            return header == b'\x89PNG\r\n\x1a\n'
    except:
        return False
