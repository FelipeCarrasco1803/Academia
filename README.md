# API de Competição de Crossfit

Este projeto é uma API assíncrona para gerenciar uma competição de crossfit, desenvolvida usando o framework FastAPI. O objetivo é criar um aplicativo web moderno e escalável que possa lidar com operações simultâneas de maneira eficiente.

## Tecnologias Utilizadas
- **Python 3.7+**
- **FastAPI**
- **Uvicorn** (servidor ASGI para execução da API)
- **SQLAlchemy** (para manipulação do banco de dados)
- **SQLite** (banco de dados utilizado para fins de desenvolvimento)

## Estrutura do Projeto
O projeto está todo concentrado em um único arquivo chamado `academia.py` para facilitar o desenvolvimento e a compreensão do código.

## Funcionalidades da API
- **Criação de Participantes:** Permite a criação de novos participantes na competição de crossfit.
- **Listagem de Participantes:** Permite listar todos os participantes cadastrados, com suporte para paginação.
- **Endpoint Raiz:** Exibe uma mensagem de boas-vindas para confirmar que a API está funcionando corretamente.

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/crossfit-api.git
   cd crossfit-api
