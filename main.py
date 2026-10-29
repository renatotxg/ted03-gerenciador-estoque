from pathlib import Path
from arquivos import ler_csv

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
if __name__ == "__main__":
    main()