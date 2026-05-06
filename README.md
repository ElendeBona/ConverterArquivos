# Conversor de Arquivo TXT para XLS

Este projeto é um script em Python que converte arquivos no formato `.txt` para `.xls` ou `.xlsx`, 
facilitando a manipulação de dados em planilhas do Excel. Ele lê os dados do arquivo `.txt`, onde 
as informações estão separadas por ponto e vírgula (`;`), e cria uma planilha Excel organizada com essas informações.

# Outro método é realizar diretamente no Excel com o Power Query 
![Método com Power Query](<Card 01 — Power Query@2x.png>)
![Excel](<tela excel.png>)
![Método Script Python](<Card 02 — Python@2x.png>)
![Python](<tela python.png>)
## Funcionalidades

- Conversão de arquivos `.txt` para `.xls` ou `.xlsx`.
- Suporte para arquivos `.txt` com dados separados por ponto e vírgula (`;`).
- Exportação para planilhas Excel sem cabeçalhos e índices.

## Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** para manipulação de dados.
- **xlwt** para exportar para `.xls` (opcional).
- **openpyxl** para exportar para `.xlsx`.

## Como Usar

1. Certifique-se de ter Python instalado.
2. Instale as dependências necessárias com `pip install pandas xlwt openpyxl`.
3. Coloque o arquivo `.txt` na mesma pasta que o script.
4. Execute o script para converter o arquivo.
5. O arquivo `.xlsx` não deve está na pasta, pode gerar erro.

```bash
python converterTxtPorXls.py
```

O arquivo convertido será salvo na mesma pasta do script.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou reportar problemas através da seção de issues.