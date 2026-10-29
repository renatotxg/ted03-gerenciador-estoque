
from pathlib import Path
from datetime import datetime
import shutil


def criar_backup(caminho):
    origem = Path(caminho)

    try:
        if not origem.is_file():
            print("Erro: arquivo original não encontrado.")
            return False

        pasta_backup = Path(__file__).resolve().parent / "backups"
        pasta_backup.mkdir(exist_ok=True)

        data = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        nome_backup = f"{origem.stem}_{data}{origem.suffix}"
        destino = pasta_backup / nome_backup

        with open(origem, "rb") as arquivo_origem:
            with open(destino, "xb") as arquivo_destino:
                shutil.copyfileobj(arquivo_origem, arquivo_destino)

        print(f"Backup realizado com sucesso: {nome_backup}")
        return True

    except FileNotFoundError:
        print("Erro: arquivo original não encontrado.")

    except PermissionError:
        print("Erro: sem permissão para realizar o backup.")

    except OSError as erro:
        print(f"Erro ao criar backup: {erro}")

    return False
