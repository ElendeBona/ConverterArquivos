import xlwt
import os
import openpyxl  # .xlsx


def txt_para_xls(arquivo_txt, arquivo_xls):
    """
    Converte um arquivo .txt para .xls

    :param arquivo_txt: caminho do arquivo .txt de entrada
    :param arquivo_xls: caminho do arquivo .xls de saída
    """
    if not os.path.isfile(arquivo_txt):
        raise FileNotFoundError(f"Arquivo não encontrado: {arquivo_txt}")

    # Detecta delimitador automaticamente pela primeira linha
    with open(arquivo_txt, "r", encoding="utf-8") as f:
        primeira_linha = f.readline()
        delimitador = "," if "," in primeira_linha else ";"

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Dados")

    with open(arquivo_txt, "r", encoding="utf-8") as f:
        for linha_idx, linha in enumerate(f):
            colunas = linha.strip().split(delimitador)
            for col_idx, valor in enumerate(colunas):
                sheet.write(linha_idx, col_idx, valor)

    workbook.save(arquivo_xls)
    print(f"Arquivo salvo em: {arquivo_xls}")


if __name__ == "__main__":
    pasta = r"C:\Users\edsoo\Downloads\dados"
    txt_para_xls(
        arquivo_txt=os.path.join(pasta, "dados.txt"),
        arquivo_xls=os.path.join(pasta, "dados.xls"),
    )
