from pathlib import Path
from arquivos import ler_csv
from conversor import csv_para_json, json_para_csv
from backup import criar_backup

def main():
    pasta = Path(__file__).resolve().parent
    caminho = pasta / "dados" / "produtos.csv"

    produtos = ler_csv(caminho)

    if produtos is not None:
        print("\n=== Estoque De Produtos ===")

        for produto in produtos:
          print(
                f"{produto['codigo']} | "
                f"{produto['nome']} | "
                f"R$ {produto['preco']} | "
                f"Estoque: {produto['quantidade']}"
            )
          caminho_json = pasta / "dados" / "produtos.json"
    csv_para_json(caminho, caminho_json)

    caminho_csv_novo = pasta / "dados" / "produtos_convertidos.csv"
    json_para_csv(caminho_json, caminho_csv_novo)

    
    original = ler_csv(caminho)
    convertido = ler_csv(caminho_csv_novo)

    if original is not None and convertido is not None:
        if original == convertido:
            print("Teste de integridade: Ok! Nenhum dado foi perdido.")
        else:
            print("Erro: os arquivos possuem dados diferentes.")
    print("\n===== TESTE DE BACKUP =====")
    criar_backup(caminho)
    
if __name__ == "__main__":
    main()