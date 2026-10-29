# TED 03 — Gerenciador de Estoque com CSV e JSON

## 1. Descrição do projeto

Este projeto foi desenvolvido em Python como parte do trabalho TED 03 Gerenciador de Persistência de Dados em Arquivos Estruturados (CSV e JSON).

O sistema permite gerenciar um pequeno estoque de produtos, realizando leitura, cadastro, atualização e conversão de dados entre os formatos CSV e JSON.

Esta aplicação também possui tratamento de exceções e um mecanismo de backup automático, visando manter os dados antes de operações que modifiquem arquivos existentes.

## 2. Integrantes

- **Integrante 1:** Daniel Veríssimo Nunes - 26.1.16160
- **Integrante 2:** Renato Guido Teixeira - 26.1.20345

**Curso:** Análise e Desenvolvimento de Sistemas

## 3. Funcionalidades

- Leitura e listagem de produtos em arquivos CSV.
- Cadastro de novos produtos.
- Atualização de preços e quantidades.
- Conversão de arquivos CSV para JSON.
- Conversão de arquivos JSON para CSV.
- Geração automática de backups antes das alterações.
- Tratamento de erros de leitura, escrita e codificação.
- Verificação da integridade dos dados após as conversões.
- Menu interativo executado pelo terminal.

## 4. Tecnologias utilizadas

- Python
- Módulo `csv`
- Módulo `json`
- Módulo `pathlib`
- Módulo `datetime`
- Módulo `shutil`
- Módulo `decimal`

O projeto utiliza bibliotecas da própria linguagem Python, sem necessidade de instalações externas.

## 5. Como executar

1. Baixe ou clone esse repositório.
2. Abra a pasta do projeto no VS Code ou em outro editor compatível
3. Verifique se o Python está instalado.
4. Abra o terminal na pasta principal do projeto.
5. Execute o comando:

```bash
python main.py
```

O programa apresentará um menu com as seguintes opções:

```text
=== Gerenciador de estoque ===
1 - Listar produtos
2 - Cadastrar produto
3 - Atualizar produto
4 - Converter CSV para JSON
5 - Converter JSON para CSV
0 - Sair
```

## 6. Organização dos arquivos

- `main.py`: menu principal e execução do programa.
- `arquivos.py`: leitura dos arquivos CSV e tratamento de erros.
- `estoque.py`: cadastro, atualização e gravação de produtos.
- `conversor.py`: conversão entre CSV e JSON.
- `backup.py`: criação de cópias de segurança.
- `teste_integridade.py`: comparação entre os arquivos CSV.
- `dados/`: armazenamento dos arquivos CSV e JSON.
- `backups/`: cópias de segurança geradas durante as operações.
- `evidencias/`: capturas de tela dos testes realizados.

## 7. Backup e segurança

Antes de modificar um arquivo existente, o sistema realiza uma cópia dos dados anteriores.

Os backups são armazenados em uma pasta específica e identificados por data e horário, permitindo diferenciar as versões preservadas.

Caso a criação do backup falhe, a operação de alteração será cancelada.

## 8. Testes realizados

Foram realizados testes envolvendo:

- Conversão de CSV para JSON.
- Conversão de JSON para CSV.
- Cadastro e atualização de produtos.
- Criação automática de backups.
- Tratamento de arquivo inexistente.
- Validação de dados informados pelo usuário.
- Comparação dos registros antes e depois das conversões.

Os resultados foram documentados por meio de capturas de tela na pasta `evidencias/`.

## 9. Relatório técnico

O repositório também contém o relatório técnico em PDF, com explicações sobre a implementação, os testes, os resultados obtidos e as referências utilizadas.