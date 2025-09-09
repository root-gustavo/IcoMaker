def is_svg(caminho_arquivo):
    """
    Retorna True se o arquivo for um SVG real.
    Verifica se começa com a tag <svg ou <?xml.
    """
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            inicio = f.read(100).lower()  # lê os primeiros 100 caracteres
            return "<svg" in inicio or "<?xml" in inicio
    except:
        return False
