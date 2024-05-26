import os

# Variáveis iniciais
texto = "test.txt"
local = "C:/Users/thayn/Desktop/Victor programacao/Projeto_Compressao_e_Descompressao_de_Dados/text/Test.txt"
caracteres_armazenados = []

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
        while i + 1 < len(texto) and texto[i] == texto[i + 1] and texto[i] == '\n' or texto[i] == " ":
            i += 1
            count += 1
        if count >= 4:
            caracteres_armazenados.append(texto[i])
            caracteres_armazenados.append(f'#{count:0{1 if count < 10 else 2}d}')
            comprimido += f"{texto[i]}#{count:0{1 if count < 10 else 2}d}"
            i+=1
        else:
            comprimido += texto[i] * count
            i += 1
    return comprimido

# Função de descompressão
def descompressao(texto):
    descomprimido = ""
    i = 0
    while i < len(texto):
        #Valida se a quantidade de letra é maior que 3
        if i + 3 < len(texto) and texto[i + 1] == '#' and texto[i + 2].isdigit() or texto[i + 2:i + 4].isdigit():
            multiplicador = verificar_multiplicador(texto, i)
            descomprimido = verificar_posicoes(texto[i], caracteres_armazenados, descomprimido,i,multiplicador)
            total_index = controlador_index(multiplicador)
            i += total_index 
        else:
            descomprimido += texto[i]
            i += 1
    return descomprimido

#
def verificar_posicoes(texto, caracteres_armazenados, descomprimido,i,multiplicador):
            for j in range(len(caracteres_armazenados)):
                if texto == caracteres_armazenados[j]: 
                    if multiplicador == caracteres_armazenados[j+1]:
                        numero = caracteres_armazenados[j+1]
                        numero = numero.replace("#", "")
                        numero = int(numero)
                        descomprimido += caracteres_armazenados[j] * numero
                        return descomprimido
                else:
                    j+=1

#Valida o número de vezes a ser posicionado uma letra
def verificar_multiplicador(texto,i):
        validador = 0
        numero = 2
        controlador = len(texto)
        while validador == 0:
            if texto[i + numero].isdigit() and i+numero+1 < controlador:
                if texto[i+numero+1].isdigit():
                    numero += 1
                else:
                    multiplicador = texto[i + 1:i + 1 + numero]
                    validador = 1
            else:     
                multiplicador = texto[i + 1:i + 1 + numero]
                validador = 1               
        return multiplicador

#Controla o número de indeices a ser pulado
def controlador_index(multiplicador):
        total = len(multiplicador)
        total += 1
        return total
     

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