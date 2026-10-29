import csv

def ler_csv(caminho):
    try:
        with open(caminho, "r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)
            produtos = list(leitor)

            return produtos

    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")

    except PermissionError:
        print("Erro: acesso ao arquivo negado.")

    except UnicodeDecodeError:
        print("Erro: problema na codificação do arquivo.")

    except (OSError, csv.Error) as erro:
        print(f"Erro ao ler o arquivo: {erro}")

    return None
