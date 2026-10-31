# Avaliação de textos alternativos em imagens de portais de notícia brasileiros

Repositório de dados e materiais de apoio de um Trabalho de Conclusão de Curso sobre a qualidade de textos alternativos (alt text) gerados por inteligência artificial para imagens jornalísticas. O estudo considera a descrição visual, o contexto da notícia e a utilidade do texto para pessoas com deficiência visual.

## Conteúdo do repositório

| Caminho | Conteúdo |
| --- | --- |
| `imagens/` | 40 imagens numeradas, em formatos como JPG, PNG e WebP. |
| `docs/Planilha Textos Alternativos.xlsx` | Planilha principal do estudo. |
| `docs/Planilha Textos Alternativos.ods` | Cópia da planilha em formato OpenDocument. |
| `docs/Planilha Textos Alternativos - Página1.pdf` | Exportação em PDF da planilha. |
| `docs/alt_text_articles/` | Material de referência sobre diretrizes de alt text, incluindo uma tese em PDF. |
| `alt_text_imagem_informativa.txt` | Exemplos de descrições de imagem informativa, organizados em versões com e sem contexto. |
| `alt_text_imagem_complexa.txt` | Exemplos de descrições de imagens complexas, com e sem contexto. |
| `Listas de Alt Texts Com e Sem Contexto/` | Planilha ODS com listas de textos alternativos para imagens informativas. |
| `comparacao_alt_texts_com_e_sem_contexto_imagem_complexas.xlsx` | Planilha de comparação de textos alternativos para imagens complexas. |
| `diferencas_alt_text_com_e_sem_contexto_imagens_complexas.docx` | Documento com diferenças entre descrições de imagens complexas com e sem contexto. |
| `urls.txt` | URLs usadas como entrada para o script de download. |
| `script.py` | Script para baixar as imagens listadas em `urls.txt`. |
| `constants/paths.py` | Definição de caminhos usados pelo projeto, incluindo diretórios de materiais de referência e imagens. |
| `pyproject.toml` e `uv.lock` | Configuração do projeto Python e arquivo de dependências travadas. |

Os arquivos de imagem são numerados para facilitar sua associação aos registros do estudo. Consulte as planilhas para os dados e avaliações completos; os arquivos de texto e documentos de comparação são materiais complementares.

## Baixar as imagens

O `script.py` lê `urls.txt` na pasta em que é executado e salva os arquivos em `imagens/`. O nome de cada arquivo usa a posição da URL na lista e a extensão identificada na URL (ou `.jpg` como padrão). O script usa a biblioteca `requests`.

Com Python 3.13 ou superior e [uv](https://docs.astral.sh/uv/) instalados:

```bash
uv sync
uv run python script.py
```

O script tenta baixar cada URL sequencialmente e informa falhas no terminal. A execução pode substituir um arquivo existente se o nome numerado coincidir.

## Dependências

As dependências declaradas em `pyproject.toml` incluem `requests`, `pandas`, `Pillow`, `python-dotenv` e `google-genai`. Para instalar o ambiente do projeto, use `uv sync`. O script de download atualmente importa `requests`; os demais pacotes estão declarados para os recursos de análise do projeto.

## Organização e configuração

`constants/paths.py` centraliza os caminhos relativos à raiz do repositório, como `docs/`, `imagens/` e `ia_requests/`. Alguns desses diretórios podem ser usados por etapas de trabalho que não estão representadas por scripts neste repositório.

## Contexto acadêmico

O projeto investiga acessibilidade digital e o uso de inteligência artificial na descrição de imagens em notícias brasileiras. Os materiais com e sem contexto permitem observar como informações da notícia podem influenciar a produção e a avaliação de descrições.
