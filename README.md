# Saas-Financeiro

# 💰 SaaS Financeiro

Sistema de gerenciamento financeiro desenvolvido em **Python + Flask**, com foco em organização, controle e visualização das movimentações financeiras.

O projeto foi desenvolvido com uma estrutura modular para facilitar a manutenção, evolução e futura transformação do sistema em um SaaS completo.

---

## 🚀 Sobre o projeto

O **SaaS Financeiro** permite registrar e acompanhar entradas e saídas financeiras, organizar transações por categorias e visualizar informações importantes através de um painel central.

A ideia do projeto é evoluir de um sistema financeiro pessoal para uma plataforma que possa ser utilizada por diferentes usuários e empresas.

### Principais objetivos

* 📊 Visualizar a situação financeira através de um Dashboard
* 💰 Registrar entradas e saídas
* 🗂️ Organizar transações por categorias
* 📑 Consultar o extrato financeiro
* ⚙️ Personalizar informações do sistema
* 📈 Trabalhar com projeções de saldo
* 🧾 Futuramente gerenciar orçamentos e serviços

---

## 🛠️ Tecnologias utilizadas

### Backend

* **Python**
* **Flask**
* **SQLite**
* **Jinja2**

### Frontend

* **HTML5**
* **JavaScript**
* **Tailwind CSS**

### Estrutura

O projeto utiliza **Blueprints/rotas separadas** para organizar as diferentes funcionalidades do sistema.

---

## 📂 Estrutura do projeto

Uma estrutura aproximada do projeto:

```text
My Project/
│
├── app.py
├── sistema.db
├── requirements.txt
│
├── functions/
│   ├── ...
│   └── ...
│
├── routes/
│   ├── show_data.py
│   ├── site_on.py
│   ├── add_categoria.py
│   ├── declarar/
│   └── ...
│
├── templates/
│   ├── dashboard.html
│   ├── declarar.html
│   ├── extrato.html
│   ├── configuracoes.html
│   └── ...
│
├── static/
│   ├── css/
│   ├── js/
│   └── ...
│
└── uploads/
    └── ...
```

> A estrutura pode mudar conforme novas funcionalidades forem adicionadas ao projeto.

---

## 📊 Dashboard

O Dashboard é responsável por apresentar uma visão geral das informações financeiras.

Entre os dados apresentados estão:

* **Saldo atual**
* **Total de entradas**
* **Total de saídas**
* **Projeção de saldo**
* **Transações recentes**
* **Informações financeiras calculadas pelo sistema**

Parte dos valores apresentados no Dashboard é atualizada dinamicamente através de JavaScript.

---

## 💵 Entradas e saídas

O sistema permite registrar movimentações financeiras classificadas como:

```text
Entrada
Saída
```

Cada movimentação pode possuir informações como:

* Nome/descrição
* Valor
* Data
* Tipo da movimentação
* Categoria

Essas informações são armazenadas no banco de dados SQLite.

---

## 🗂️ Categorias

O sistema possui gerenciamento de categorias para facilitar a organização das movimentações.

Exemplo:

```text
Entradas
├── Salário
├── Vendas
├── Serviços
└── Outros

Saídas
├── Alimentação
├── Transporte
├── Contas
├── Lazer
└── Outros
```

As categorias podem ser utilizadas durante o cadastro das transações.

---

## 📑 Extrato

A página de **Extrato** permite consultar as movimentações registradas no sistema.

O objetivo é fornecer uma visão organizada do histórico financeiro, permitindo acompanhar entradas e saídas realizadas.

---

## ⚙️ Configurações

A área de configurações permite personalizar informações do sistema.

Entre as funcionalidades planejadas/implementadas estão:

* Alteração do nome do sistema
* Alteração da logo
* Visualização da logo
* Personalização da identificação do sistema
* Gerenciamento de categorias

A personalização permite que o sistema possa futuramente ser adaptado para diferentes usuários ou empresas.

---

## 🧾 Orçamentos

Uma das funcionalidades em desenvolvimento é o módulo de **Orçamentos**.

A proposta é permitir criar orçamentos para clientes utilizando serviços cadastrados no sistema.

Exemplo:

```text
Serviço: Banner
Largura: 2m
Altura: 1m
Preço por m²: R$ 50,00

Total: R$ 100,00
```

O sistema poderá realizar cálculos automaticamente a partir das medidas e preços cadastrados.

Esse módulo também terá um sistema próprio de categorias de serviços, separado das categorias utilizadas nas movimentações financeiras.

---

## 🗄️ Banco de dados

O projeto utiliza **SQLite** como banco de dados.

O arquivo principal atualmente é:

```text
sistema.db
```

A utilização do SQLite facilita o desenvolvimento e permite que o sistema funcione sem a necessidade de configurar um servidor de banco de dados externo.

No futuro, o projeto poderá utilizar um banco de dados mais robusto caso seja necessário suportar múltiplos usuários e maior volume de dados.

---

## 🔐 Segurança

O projeto ainda está em desenvolvimento e algumas funcionalidades de segurança estão previstas para versões futuras.

Entre elas:

* Sistema de autenticação
* Controle de usuários
* Permissões
* Proteção de dados
* Separação dos dados entre usuários
* Configuração segura de produção

> **Importante:** o projeto não deve ser considerado pronto para produção enquanto essas medidas não estiverem devidamente implementadas e testadas.

---

## ▶️ Como executar

### 1. Clone o projeto

```bash
git clone SEU_REPOSITORIO
```

Entre na pasta:

```bash
cd "My Project"
```

### 2. Crie um ambiente virtual

Windows:

```bash
python -m venv venv
```

Ative o ambiente:

```bash
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o projeto

```bash
python app.py
```

Depois, acesse no navegador:

```text
http://127.0.0.1:5000
```

---

## 📦 Dependências

As principais dependências do projeto podem ser instaladas através do arquivo:

```text
requirements.txt
```

Exemplo:

```text
Flask
```

Outras bibliotecas podem ser adicionadas conforme novas funcionalidades forem implementadas.

---

## 🧠 Arquitetura

O projeto busca manter uma separação entre:

```text
Rotas
   ↓
Funções / Regras
   ↓
Banco de dados
   ↓
Templates / JavaScript
```

Essa organização facilita a manutenção e permite adicionar novas funcionalidades sem concentrar toda a lógica em um único arquivo.

---

## 🔮 Roadmap

### ✅ Atualmente

* [x] Dashboard
* [x] Registro de entradas
* [x] Registro de saídas
* [x] Categorias
* [x] Extrato
* [x] Configurações
* [x] Personalização do nome do sistema
* [x] Personalização da logo
* [x] Banco de dados SQLite

### 🚧 Em desenvolvimento

* [ ] Sistema de Orçamentos
* [ ] Cadastro de serviços
* [ ] Cálculo automático por medidas
* [ ] Categorias específicas para serviços
* [ ] Edição de declarações existentes
* [ ] Melhorias no Dashboard

### 🔮 Futuro

* [ ] Sistema de usuários
* [ ] Login e autenticação
* [ ] Multiusuário
* [ ] Sistema de assinatura
* [ ] Banco de dados para produção
* [ ] API
* [ ] Deploy em servidor
* [ ] Relatórios financeiros
* [ ] Exportação de dados
* [ ] Backup automático
* [ ] Aplicação mobile

---

## 📈 Objetivo do projeto

O objetivo final é transformar o projeto em um **SaaS financeiro completo**, permitindo que diferentes usuários possam utilizar a plataforma para controlar suas finanças e, futuramente, administrar orçamentos e serviços.

A arquitetura está sendo desenvolvida pensando na possibilidade de transformar o projeto em uma aplicação escalável, mantendo o código organizado e facilitando a adição de novas funcionalidades.

---

## 👨‍💻 Desenvolvimento

Projeto desenvolvido utilizando **Python, Flask, SQLite, JavaScript e Tailwind CSS**.

O sistema está em desenvolvimento contínuo e novas funcionalidades serão adicionadas conforme a evolução do projeto.

---

## 📄 Licença

Este projeto ainda não possui uma licença definida.

Caso o projeto seja disponibilizado publicamente, recomenda-se definir uma licença adequada antes de permitir reutilização ou distribuição do código.
