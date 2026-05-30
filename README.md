# TCC - Avaliação de Textos Alternativos em Portais de Notícia Brasileira

## 📋 Sobre o Projeto

Este repositório contém dados e recursos para meu Trabalho de Conclusão de Curso (TCC), que avalia a qualidade de **textos alternativos (alt text) gerados por inteligência artificial** em imagens de portais de notícia brasileiros.

### Objetivo

O projeto tem como objetivo analisar e avaliar a eficácia dos textos alternativos produzidos por sistemas de IA em descrever imagens de artigos de notícias, considerando critérios de:
- Precisão descritiva
- Relevância contextual
- Acessibilidade
- Qualidade de descrição para usuários com deficiência visual

## 📁 Estrutura do Repositório

```
.
├── imagens/                                          # Diretório contendo todas as imagens coletadas
├── Planilha Textos Alternativos.xlsx                # Dados do estudo em formato Excel
├── Planilha Textos Alternativos.ods                 # Dados do estudo em formato ODS (LibreOffice)
├── Planilha Textos Alternativos - Página1.pdf       # Versão em PDF dos dados
├── script.py                                         # Script para download automático das imagens
├── urls.txt                                          # Arquivo contendo as URLs das imagens
├── pyproject.toml                                    # Configuração do projeto Python
├── README.md                                         # Este arquivo
└── .python-version                                   # Versão Python utilizada
```

## 🖼️ Dados do Estudo

As planilhas (`xlsx`, `ods` e `pdf`) contêm informações estruturadas sobre as imagens coletadas, incluindo:

- **Link da notícia**: URL da página de origem da imagem
- **Título da notícia**: Título do artigo
- **Descrição da imagem**: Informações adicionais sobre a imagem
- **Texto alternativo gerado**: Alt text produzido pelo sistema de IA
- **Avaliação qualitativa**: Análise e métricas de qualidade
- Outras metadatas relevantes para o estudo

## 🖼️ Diretório de Imagens

O diretório `imagens/` contém todas as imagens coletadas dos portais de notícia brasileiros, usadas para análise de textos alternativos gerados por IA. Cada imagem está nomeada sequencialmente para facilitar referência cruzada com os dados nas planilhas.

## 🚀 Script de Download

### `script.py`

Script Python que automatiza o download das imagens a partir das URLs listadas em `urls.txt`.

**Funcionalidades:**
- Lê URLs do arquivo `urls.txt`
- Faz download automático das imagens
- Salva as imagens no diretório `imagens/`
- Mantém a extensão de arquivo original
- Trata erros de download e exceções

**Uso:**

```bash
# Instalando dependências
uv sync

# Executando o script
python script.py
```

### Arquivo `urls.txt`

Contém uma lista de URLs, uma por linha, das imagens a serem baixadas. O script processa este arquivo sequencialmente para fazer download de todas as imagens.

## 📦 Dependências

O projeto utiliza Python 3.13+ e as seguintes dependências:

- **requests** (>=2.34.2): Para realizar requisições HTTP e download de imagens

### Instalação

1. Garanta que você tem Python 3.13+ instalado
2. Clone este repositório
3. Instale as dependências usando `uv`:

```bash
uv sync
```

## 💻 Tecnologias Utilizadas

- **Python 3.13+**: Linguagem de programação principal
- **requests**: Biblioteca para download de imagens
- **uv**: Package manager para Python
- **LibreOffice/Excel**: Para análise de dados em planilhas
- **PDF**: Formato de relatório e documentação

## 📊 Dados Coletados

Total de imagens analisadas: Veja o diretório `imagens/` para quantidade exata

Todos os dados estão documentados nas planilhas fornecidas em múltiplos formatos para compatibilidade e acessibilidade.

## 🎓 Contexto Acadêmico

Este projeto faz parte de um estudo acadêmico sobre acessibilidade web e inteligência artificial, focando especificamente em como sistemas de IA descrevem imagens em contextos de jornalismo digital brasileiro, contribuindo para a compreensão de como melhorar a acessibilidade de conteúdo digital.

---

**Autor**: Trabalho de Conclusão de Curso (TCC)  
**Data**: 2026