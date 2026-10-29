import csv
import json
from pathlib import Path
from arquivos import ler_csv
from backup import criar_backup

def csv_para_json(caminho_csv, caminho_json):
    produtos = ler_csv(caminho_csv)

    if produtos is None:
        print("Não foi possível realizar a conversão.")
        return

    try:
        destino = Path(caminho_json)

        if destino.exists():
            if not criar_backup(destino):
                print("Conversão cancelada: falha no backup.")
                return

        with open(destino, "w", encoding="utf-8") as arquivo:
            json.dump(produtos, arquivo, indent=4, ensure_ascii=False)

        print("Arquivo convertido para JSON com sucesso!")

    except PermissionError:
        print("Erro: sem permissão para criar o arquivo JSON.")

    except (OSError, TypeError, ValueError) as erro:
        print(f"Erro durante a conversão: {erro}")


def json_para_csv(caminho_json, caminho_csv):
    try:
        with open(caminho_json, "r", encoding="utf-8") as arquivo:
            produtos = json.load(arquivo)

        if not isinstance(produtos, list) or not produtos:
            print("Erro: o JSON deve conter uma lista de produtos.")
            return

        if not all(isinstance(p, dict) for p in produtos):
            print("Erro: os produtos devem ser objetos JSON.")
            return

        campos = list(produtos[0].keys())

        if not all(set(p.keys()) == set(campos) for p in produtos):
            print("Erro: os produtos possuem campos diferentes.")
            return

        destino = Path(caminho_csv)

        if destino.exists():
            if not criar_backup(destino):
                print("Conversão cancelada: falha no backup.")
                return

        with open(destino, "w", encoding="utf-8", newline="") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(produtos)

        print("Arquivo convertido para CSV com sucesso!")

    except FileNotFoundError:
        print("Erro: arquivo JSON não encontrado.")

    except PermissionError:
        print("Erro: acesso ao arquivo negado.")

    except UnicodeDecodeError:
        print("Erro: problema na codificação do arquivo.")

    except json.JSONDecodeError:
        print("Erro: o arquivo JSON possui formato inválido.")

    except (OSError, csv.Error, ValueError, TypeError) as erro:
        print(f"Erro durante a conversão: {erro}")
