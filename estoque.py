
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path
from arquivos import ler_csv
from backup import criar_backup


CAMPOS = ["codigo", "nome", "categoria", "preco", "quantidade"]


def salvar_produtos(caminho, produtos):
    destino = Path(caminho)

    # Faz o backup antes de modificar um arquivo existente
    if destino.exists():
        if not criar_backup(destino):
            print("Alteração cancelada: falha no backup.")
            return False

    try:
        with open(destino, "w", encoding="utf-8", newline="") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(produtos)

        print("Dados salvos com sucesso!")
        return True

    except (PermissionError, OSError, csv.Error, ValueError) as erro:
        print(f"Erro ao salvar os dados: {erro}")
        return False


def cadastrar_produto(caminho):
    produtos = ler_csv(caminho)

    if produtos is None:
        print("Não foi possível acessar o estoque.")
        return

    print("\n === Cadastrar Produto ===")

    codigo = input("Código: ").strip()
    nome = input("Nome: ").strip()
    categoria = input("Categoria: ").strip()
    preco = input("Preço: ").strip().replace(",", ".")
    quantidade = input("Quantidade: ").strip()

    if not codigo or not nome or not categoria:
        print("Erro: código, nome e categoria são obrigatórios.")
        return

    if any(p["codigo"] == codigo for p in produtos):
        print("Erro: já existe um produto com esse código.")
        return

    try:
        valor = Decimal(preco)

        if not valor.is_finite() or valor < 0:
            print("Erro: informe um preço válido.")
            return

        if not quantidade.isdigit():
            print("Erro: a quantidade deve ser um número inteiro positivo.")
            return

    except InvalidOperation:
        print("Erro: preço inválido.")
        return

    novo_produto = {
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "preco": f"{valor:.2f}",
        "quantidade": quantidade
    }

    produtos.append(novo_produto)

    if salvar_produtos(caminho, produtos):
        print("Produto cadastrado com sucesso")



def atualizar_produto(caminho):
    produtos = ler_csv(caminho)

    if produtos is None:
        print("Não foi possível acessar o estoque.")
        return

    print("\n === Atualizar produto ===")
    codigo = input("Digite o código do produto: ").strip()

    produto = next(
        (p for p in produtos if p["codigo"] == codigo),
        None
    )

    if produto is None:
        print("Erro: produto não encontrado.")
        return

    print(f"\nProduto: {produto['nome']}")
    print(f"Preço atual: R$ {produto['preco']}")
    print(f"Quantidade atual: {produto['quantidade']}")

    print("\nDeixe em branco para manter o valor atual.")

    novo_preco = input("Novo preço: ").strip().replace(",", ".")
    nova_quantidade = input("Nova quantidade: ").strip()

    if not novo_preco and not nova_quantidade:
        print("Nenhuma alteração realizada.")
        return

    try:
        if novo_preco:
            valor = Decimal(novo_preco)

            if not valor.is_finite() or valor < 0:
                print("Erro: preço inválido.")
                return

            novo_preco = f"{valor:.2f}"

        if nova_quantidade and not nova_quantidade.isdigit():
            print("Erro: quantidade inválida.")
            return

    except InvalidOperation:
        print("Erro: informe um preço válido.")
        return

    if novo_preco:
        produto["preco"] = novo_preco

    if nova_quantidade:
        produto["quantidade"] = nova_quantidade

    if salvar_produtos(caminho, produtos):
        print("Produto atualizado com sucesso!")

    