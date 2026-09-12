# Organização do SaaS Financeiro

Esta versão organiza o projeto sem reescrever a lógica principal.

## Estrutura

- `app.py` — inicia o Flask e registra as rotas.
- `routes/` — URLs do sistema. Cada arquivo representa uma área.
  - `site.py` — página inicial.
  - `lancamentos.py` — salvar lançamentos financeiros.
  - `categorias.py` — categorias, obras e dados do dashboard.
  - `extrato.py` — filtros do extrato.
  - `download.py` — backup/download do banco.
  - `produtos.py` — espaço reservado para produtos.
- `database/` — conexão e criação das tabelas SQLite.
- `functions/` — funções auxiliares usadas pela aplicação.
- `templates/` — HTML.
- `uploads/` — arquivos enviados pelo sistema.

## Organização das URLs

As URLs também foram agrupadas por responsabilidade:

- `/` → página inicial
- `/lancamentos/salvar` → salvar lançamento
- `/categorias/...` → categorias, obras e dados relacionados
- `/extrato/filtrar` → filtro do extrato
- `/sistema/backup` → download do banco

O HTML foi atualizado para usar as novas URLs.

## Nomes internos

Alguns nomes foram melhorados apenas quando ficavam mais claros, como:

- `projetion_saldo` → `projecao_saldo`
- `filter` → `filtrar_transacoes`

Foram mantidos aliases antigos para reduzir o risco de quebrar chamadas existentes.

## Regra desta organização

A ideia é deixar o projeto fácil de entender enquanto você continua desenvolvendo.

Não foram adicionadas camadas complexas como repository/service/controller apenas por organização.
