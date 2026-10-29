
from pathlib import Path
from arquivos import ler_csv

pasta = Path(__file__).resolve().parent

original = pasta / "dados" / "produtos.csv"
convertido = pasta / "dados" / "produtos_convertidos.csv"

dados_originais = ler_csv(original)
dados_convertidos = ler_csv(convertido)

print("\n === Teste de integridade === ")

if dados_originais is None or dados_convertidos is None:
    print("Não foi possível realizar a comparação.")

elif dados_originais == dados_convertidos:
    print("Teste aprovado!")
    print("Todos os registros e valores foram preservados.")
    print(f"Total de produtos: {len(dados_originais)}")

else:
    print("Teste reprovado: existem diferenças entre os arquivos.")
