import os

# Variáveis iniciais
texto = "test.txt"
local = "D:/Victor/Programação/Projeto_Compressao_e_Descompressao_de_Dados/text/test.txt"

# Função para ler o arquivo
def ler_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as file:
        return file.read()

# Função para escrever no arquivo
def escrever_arquivo(caminho, conteudo):
    with open(caminho, 'w', encoding='utf-8') as file:
        file.write(conteudo)

# Função de compressão
def compressao(texto):
    comprimido = ""
    i = 0
    while i < len(texto):
        count = 1
        while i + 1 < len(texto) and texto[i] == texto[i + 1]:
            i += 1
            count += 1
        if count >= 4:
            comprimido += f"{texto[i]}#{count:02d}"
        else:
            comprimido += texto[i] * count
        i += 1
    comprimido = comprimido.replace(" ", "@")  # Marca espaços com @@
    comprimido = comprimido.replace("\n", "#") # Marca novas linhas com ##
    return comprimido

# Função de descompressão
def descompressao(texto):
    descomprimido = ""
    i = 0
    while i < len(texto):
        if texto[i:i+1] == '@':
            if texto[i+1] == '#' and texto[i + 2:i + 4].isdigit():
                char = texto[i]
                char = char.replace("@", " ")
                count = int(texto[i + 2:i + 4])
                descomprimido += char * count
                i += 4
            else:
                descomprimido += ' '
                i += 1
        elif texto[i:i+1] == '#':
            descomprimido += '\n'
            i += 1
        elif i + 3 < len(texto) and texto[i + 1] == '#' and texto[i + 2:i + 4].isdigit():
            char = texto[i]
            count = int(texto[i + 2:i + 4])
            descomprimido += char * count
            i += 4
        else:
            descomprimido += texto[i]
            i += 1
    return descomprimido

# Caminho dos arquivos
caminho_original = local
base_nome = os.path.splitext(texto)[0]
caminho_comprimido = os.path.join(os.path.dirname(local), f"{base_nome}_comprimido.txt")
caminho_descomprimido = os.path.join(os.path.dirname(local), f"{base_nome}_descomprimido.txt")

# Leitura do arquivo original
conteudo_original = ler_arquivo(caminho_original)

# Compressão do conteúdo
conteudo_comprimido = compressao(conteudo_original)

# Descompressão do conteúdo comprimido
conteudo_descomprimido = descompressao(conteudo_comprimido)

# Escrita dos arquivos comprimido e descomprimido
escrever_arquivo(caminho_comprimido, conteudo_comprimido)
escrever_arquivo(caminho_descomprimido, conteudo_descomprimido)

# Cálculo da taxa de compressão
caracteres_original = len(conteudo_original)
caracteres_comprimido = len(conteudo_comprimido)
taxa_compressao = (1 - (caracteres_comprimido / caracteres_original)) * 100

# Exibição dos resultados
print(f"Taxa de compressão: {taxa_compressao:.2f}%")
print(f"Arquivo original: {caracteres_original} caracteres")
print(f"Arquivo comprimido: {caracteres_comprimido} caracteres")