class Produto:
    def __init__(self, codigo, nome, tipo, preco, setor, desconto, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.preco = preco
        self.setor = setor
        self.desconto = desconto
        self.quantidade = quantidade

    def __str__(self):
        return (f"Código: {self.codigo}\n"
                f"Nome: {self.nome}\n"
                f"Tipo: {self.tipo}\n"
                f"Preço: R${self.preco:.2f}\n"
                f"Setor: {self.setor}\n"
                f"Desconto: {self.desconto}%\n"
                f"Quantidade: {self.quantidade}\n")


class SistemaMercado:
    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self):
        codigo = input("Informe o código do produto: ")
        nome = input("Informe o nome do produto: ")
        tipo = input("Informe o tipo do produto (ex: comida, bebida): ")
        preco = float(input("Informe o preço do produto: "))
        setor = input("Informe o setor do produto: ")
        desconto = float(input("Informe o desconto (em %): "))
        quantidade = int(input("Informe a quantidade em estoque: "))

        # Verificar se o código é único
        if any(prod.codigo == codigo for prod in self.produtos):
            print("Erro: Código do produto já existe.")
            return

        novo_produto = Produto(codigo, nome, tipo, preco, setor, desconto, quantidade)
        self.produtos.append(novo_produto)
        print("Produto cadastrado com sucesso!\n")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.\n")
        else:
            for produto in self.produtos:
                print(produto)
                print("---------------------------")

    def buscar_produto(self):
        codigo = input("Informe o código do produto para buscar: ")
        for produto in self.produtos:
            if produto.codigo == codigo:
                print("Produto encontrado:")
                print(produto)
                return
        print("Produto não encontrado.\n")

    def excluir_produto(self):
        codigo = input("Informe o código do produto para excluir: ")
        for i, produto in enumerate(self.produtos):
            if produto.codigo == codigo:
                del self.produtos[i]
                print("Produto excluído com sucesso!\n")
                return
        print("Produto não encontrado.\n")

    def editar_produto(self):
        codigo = input("Informe o código do produto para editar: ")
        for produto in self.produtos:
            if produto.codigo == codigo:
                print("Editando produto...")
                produto.nome = input("Informe o novo nome: ")
                produto.tipo = input("Informe o novo tipo: ")
                produto.preco = float(input("Informe o novo preço: "))
                produto.setor = input("Informe o novo setor: ")
                produto.desconto = float(input("Informe o novo desconto (em %): "))
                produto.quantidade = int(input("Informe a nova quantidade em estoque: "))
                print("Produto editado com sucesso!\n")
                return
        print("Produto não encontrado.\n")

    def salvar_dados(self, arquivo="produtos.txt"):
        with open(arquivo, 'w') as f:
            for produto in self.produtos:
                f.write(f"{produto.codigo},{produto.nome},{produto.tipo},{produto.preco},{produto.setor},{produto.desconto},{produto.quantidade}\n")
        print("Dados salvos com sucesso!\n")

    def carregar_dados(self, arquivo="produtos.txt"):
        try:
            with open(arquivo, 'r') as f:
                for linha in f:
                    codigo, nome, tipo, preco, setor, desconto, quantidade = linha.strip().split(',')
                    self.produtos.append(Produto(codigo, nome, tipo, float(preco), setor, float(desconto), int(quantidade)))
            print("Dados carregados com sucesso!\n")
        except FileNotFoundError:
            print("Arquivo não encontrado.\n")


# Exemplo de uso do sistema
sistema = SistemaMercado()

while True:
    print("Menu:")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Buscar produto")
    print("4. Excluir produto")
    print("5. Editar produto")
    print("6. Salvar dados")
    print("7. Carregar dados")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        sistema.cadastrar_produto()
    elif opcao == '2':
        sistema.listar_produtos()
    elif opcao == '3':
        sistema.buscar_produto()
    elif opcao == '4':
        sistema.excluir_produto()
    elif opcao == '5':
        sistema.editar_produto()
    elif opcao == '6':
        sistema.salvar_dados()
    elif opcao == '7':
        sistema.carregar_dados()
    elif opcao == '0':
        print("Encerrando o sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.\n")