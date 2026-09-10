# 📊 Budget App (Aplicação de Orçamento)

Este projeto é uma aplicação de gerenciamento de orçamento desenvolvida em Python. O sistema permite criar diferentes categorias de despesas, registrar depósitos, retiradas, transferências entre contas e gerar um gráfico de barras com a porcentagem de gastos por categoria.

---

## 🎯 Origem e Propósito

Este projeto faz parte do desafio prático do currículo **[Scientific Computing with Python](https://www.freecodecamp.org/)** da plataforma **freeCodeCamp**.

O objetivo principal do exercício foi praticar:
- Programação Orientada a Objetos (POO) em Python.
- Manipulação de listas e dicionários.
- Formatação avançada de strings e alinhamento visual no terminal.
- Validação e lógica de saldo/fundos.

---

## 🚀 Funcionalidades

- **Classe `Category`**:
  - `deposit(amount, description)`: Registra depósitos no livro de razão (*ledger*).
  - `withdraw(amount, description)`: Registra saídas caso haja saldo suficiente.
  - `get_balance()`: Retorna o saldo atual da categoria.
  - `transfer(amount, category)`: Transfere valores entre categorias diferentes.
  - `check_funds(amount)`: Retorna se há saldo disponível para a operação.
  - **Representação em String**: Exibe os lançamentos de forma formatada e alinhada ao imprimir a classe.

- **Função `create_spend_chart(categories)`**:
  - Gera um gráfico em formato textual no terminal indicando a porcentagem de gastos (saídas) de cada categoria em relação ao total gasto.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** (sem bibliotecas externas)

---

## 💻 Como Executar

1. Clone este repositório:
   ```bash
   git clone [https://github.com/brumarcuz/budget-app-python.git](https://github.com/brumarcuz/budget-app-python.git)
