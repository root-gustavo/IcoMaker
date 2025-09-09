from src.core import selecionar_arquivo, detectar_arquivo
from src.util.detect_size_img import obter_tamanho_imagem
from src.core.convert_file.convert_to_icon import converter_para_ico
import time
import os

def main():
    print("Selecione uma imagem para ser usada: \n")
    time.sleep(1)

    # Seleciona arquivo (retorna caminho completo)
    caminho_arquivo = selecionar_arquivo()
    if not caminho_arquivo:
        print("Nenhum arquivo selecionado ou arquivo não reconhecido.")
        return  # interrompe o programa

    # Mostra apenas o nome do arquivo
    print(f"Arquivo selecionado: {os.path.basename(caminho_arquivo)}")

    # Detecta tipo usando caminho completo
    tipo = detectar_arquivo(caminho_arquivo)
    if tipo:
        print(f"Tipo de arquivo detectado: {tipo}")

        # Detecta tamanho da imagem
        tamanho = obter_tamanho_imagem(caminho_arquivo)
        if tamanho:
            print(f"Tamanho da imagem: {tamanho[0]}x{tamanho[1]}")
        else:
            print("Não foi possível obter o tamanho da imagem.")

        # Converte para .ico
        caminho_ico = converter_para_ico(caminho_arquivo)
        if caminho_ico:
            print(f"Conversão concluída! Ícone salvo em: {caminho_ico}")
        else:
            print("Falha ao converter a imagem para .ico.")

    else:
        print("Tipo de arquivo não suportado.")

    input("Precione ENTER para sair.")

if __name__ == "__main__":
    main()
