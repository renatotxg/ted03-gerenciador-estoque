
from pathlib import Path
from arquivos import ler_csv
from estoque import cadastrar_produto, atualizar_produto
from conversor import csv_para_json, json_para_csv

def listar_produtos(caminho):
    produtos = ler_csv(caminho)

    if produtos is None:
        return

    print("\n === Estoque de produtos === ")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(
            f"{produto['codigo']} | "
            f"{produto['nome']} | "
            f"R$ {produto['preco']} | "
            f"Estoque: {produto['quantidade']}"
        )


def main():
    pasta = Path(__file__).resolve().parent

    caminho_csv = pasta / "dados" / "produtos.csv"
    caminho_json = pasta / "dados" / "produtos.json"
    caminho_convertido = pasta / "dados" / "produtos_convertidos.csv"

    while True:
        print("\n === Gerenciador de estoque === ")
        print("1 - Listar produtos")
        print("2 - Cadastrar produto")
        print("3 - Atualizar produto")
        print("4 - Converter CSV para JSON")
        print("5 - Converter JSON para CSV")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            listar_produtos(caminho_csv)

        elif opcao == "2":
            cadastrar_produto(caminho_csv)

        elif opcao == "3":
            atualizar_produto(caminho_csv)

        elif opcao == "4":
            csv_para_json(caminho_csv, caminho_json)

        elif opcao == "5":
            json_para_csv(caminho_json, caminho_convertido)

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
