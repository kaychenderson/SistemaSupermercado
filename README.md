# SistemaSupermercado

## 🛒 Descrição

Este projeto implementa um sistema de gerenciamento de supermercado em Python. Ele oferece funcionalidades completas, como **cadastro**, **busca**, **edição** e **exclusão de produtos**, além de permitir a **compra de itens**. O sistema também inclui o **controle de estoque**, o **gerenciamento de vendas**, e a possibilidade de **avaliar produtos**. Adicionalmente, conta com mecanismos de autenticação para diferentes perfis de usuários, como **clientes** e **administradores**, garantindo um controle eficaz e seguro das operações.

## ⚙ Funcionalidades

### 🙋‍♂️ **Cliente:**
- **Login e Cadastro**: Autenticação e registro de novos usuários.
- **Listagem de Produtos**: Exibição de produtos disponíveis no supermercado.
- **Busca de Produtos**: Pesquisa de produtos por código ou setor.
- **Realização de Compras**: Adiciona produtos ao carrinho e efetua compras.
- **Avaliação de Produtos**: Permite que o usuário adicione avaliações aos produtos.

### 👨‍💼 **Administrador:**
- **Gestão de Produtos**: Cadastro, edição, exclusão e listagem de produtos.
- **Controle de Estoque**: Exibição de produtos com estoque abaixo de um limite definido.
- **Relatório de Vendas**: Exibição do histórico de vendas realizadas.

## 📦 Instalação

Para usar o sistema, siga as etapas abaixo para instalação:

### 1. **Clone este repositório:**

```bash
git clone https://github.com/kaychenderson/SistemaSupermercado.git
```

### 2. Acesse o diretório do projeto:
```bash
cd SistemaSupermercado
```

### 3. Execute o sistema:
Basta executar o arquivo principal do sistema:

```bash
python smercado.py
```
## 💡 Como Usar

### 1. Login:

Quando o sistema for iniciado, você será solicitado a fazer login. O sistema oferece uma conta administrativa padrão:

Email: admin@gmail.com            
Senha: admin123                 
*Você também pode criar novos usuários comuns após o login, se desejar.*            

### 2. Menu do Administrador:
Após o login como administrador, você terá acesso às seguintes opções:

Cadastrar, editar, buscar e excluir produtos.
Salvar dados após efetuar alguma operação.
Visualizar e controlar o estoque.
Visualizar relatórios de vendas.

### 3. Menu do Cliente:
Após o login como administrador, você terá acesso às seguintes opções:

Listar, buscar e avaliar produtos.
Realizar compras.

## 💾 Armazenamento de Dados
Os dados do sistema são armazenados em um arquivo produtos.txt, que é carregado automaticamente quando o sistema é iniciado e salvo quando há alterações nos produtos ou no estoque.

Exemplo de arquivo produtos.txt:
```bash
001,Arroz,Comida,5.99,Alimentos,10,100
002,Coca,Bebida,3.50,Bebidas,5,50
003,Shampoo,Higiene,12.00,Higiene,0,30
```

## 🛠️ Estrutura do Código
O código foi organizado em classes principais que definem o comportamento do sistema:

### Classe Usuario: 
Responsável por armazenar as informações de login e as permissões do usuário.
### Classe Produto: 
Gerencia os atributos e comportamentos dos produtos, incluindo o cálculo de preços com desconto e a adição de avaliações.
### Classe SistemaMercado: 
Controla toda a lógica do sistema, incluindo o login, cadastro de usuários, gestão de produtos e vendas.