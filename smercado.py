class Usuario:
    def __init__(self, email, senha, is_admin=False):
        self.email = email
        self.senha = senha
        self.is_admin = is_admin

class Produto:
    def __init__(self, codigo, nome, tipo, preco, setor, desconto, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.preco = preco
        self.setor = setor
        self.desconto = desconto
        self.quantidade = quantidade
        self.avaliacoes = []

    def calcular_preco_com_desconto(self):
        return self.preco * (1 - self.desconto / 100)

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def __str__(self):
        return (f"Código: {self.codigo}\n"
                f"Nome: {self.nome}\n"
                f"Tipo: {self.tipo}\n"
                f"Preço: R${self.preco:.2f}\n"
                f"Setor: {self.setor}\n"
                f"Desconto: {self.desconto}%\n"
                f"Quantidade: {self.quantidade}\n"
                f"Avaliações: {self.avaliacoes}\n")

class SistemaMercado:
    def __init__(self):
        self.produtos = []
        self.usuarios = {
            "admin@gmail.com": Usuario("admin@gmail.com", "admin123", is_admin=True)
        }
        self.usuario_logado = None
        self.vendas = []
        self.carregar_dados() 

    def login(self):
        email = input("Informe o email: ")
        senha = input("Informe a senha: ")

        if email not in self.usuarios:
            print("Usuário não encontrado. Deseja se cadastrar como usuário comum? (s/n)")
            if input().lower() == 's':
                self.cadastrar_usuario(email, senha)
            else:
                return False

        usuario = self.usuarios.get(email)
        if usuario and usuario.senha == senha:
            self.usuario_logado = usuario
            print("Login realizado com sucesso!\n")
            if usuario.is_admin:
                self.menu_administrador()
            else:
                self.menu_usuario()
            return True
        else:
            print("Email ou senha incorretos.")
            return False

    def cadastrar_usuario(self, email=None, senha=None):
        if not email:
            email = input("Informe o email do novo usuário: ")
            senha = input("Informe a senha: ")
        self.usuarios[email] = Usuario(email, senha)
        print("Usuário cadastrado com sucesso!\n")

    def carregar_dados(self, arquivo="produtos.txt"):
        try:
            with open(arquivo, 'r') as f:
                for linha in f:
                    codigo, nome, tipo, preco, setor, desconto, quantidade = linha.strip().split(',')
                    self.produtos.append(Produto(codigo, nome, tipo, float(preco), setor, float(desconto), int(quantidade)))
            print("Dados carregados com sucesso!\n")
        except FileNotFoundError:
            print("Arquivo não encontrado.\n")

    def salvar_dados(self, arquivo="produtos.txt"):
        with open(arquivo, 'w') as f:
            for produto in self.produtos:
                f.write(f"{produto.codigo},{produto.nome},{produto.tipo},{produto.preco},{produto.setor},{produto.desconto},{produto.quantidade}\n")
        print("Dados salvos com sucesso!\n")

    def cadastrar_produto(self):
        codigo = input("Informe o código do produto: ")
        nome = input("Informe o nome do produto: ")
        tipo = input("Informe o tipo do produto (ex: comida, bebida): ")
        preco = float(input("Informe o preço do produto: "))
        setor = input("Informe o setor do produto: ")
        desconto = float(input("Informe o desconto (em %): "))
        quantidade = int(input("Informe a quantidade em estoque: "))

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

    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def buscar_produto_setor(self, setor):
        return [produto for produto in self.produtos if produto.setor == setor]

    def excluir_produto(self):
        codigo = input("Informe o código do produto a ser excluído: ")
        produto = self.buscar_produto(codigo)
        if produto:
            self.produtos.remove(produto)
            print("Produto excluído com sucesso!\n")
        else:
            print("Produto não encontrado.\n")

    def editar_produto(self):
        codigo = input("Informe o código do produto a ser editado: ")
        produto = self.buscar_produto(codigo)
        if produto:
            produto.nome = input("Novo nome do produto: ")
            produto.tipo = input("Novo tipo do produto: ")
            produto.preco = float(input("Novo preço do produto: "))
            produto.setor = input("Novo setor do produto: ")
            produto.desconto = float(input("Novo desconto do produto: "))
            produto.quantidade = int(input("Nova quantidade em estoque: "))
            print("Produto editado com sucesso!\n")
        else:
            print("Produto não encontrado.\n")

    def controle_estoque(self):
        limite = int(input("Informe o limite para estoque baixo: "))
        for produto in self.produtos:
            if produto.quantidade < limite:
                print(produto)
                print("---------------------------")

    def relatorio_vendas(self):
        if not self.vendas:
            print("Nenhuma venda realizada.\n")
        else:
            for venda in self.vendas:
                print(venda)
            print(f"Total de vendas: R${sum(venda['valor'] for venda in self.vendas):.2f}\n")

    def realizar_compra(self):
        if not self.usuario_logado:
            print("Você precisa estar logado para realizar uma compra.")
            return

        codigo = input("Informe o código do produto que deseja comprar: ")
        quantidade_desejada = int(input("Informe a quantidade: "))

        produto = self.buscar_produto(codigo)
        if produto:
            if produto.quantidade < quantidade_desejada:
                print("Estoque insuficiente.")
                return
            
            preco_total = produto.calcular_preco_com_desconto() * quantidade_desejada
            produto.quantidade -= quantidade_desejada
            self.vendas.append({"produto": produto.nome, "quantidade": quantidade_desejada, "valor": preco_total})
            print(f"Compra realizada! Total: R${preco_total:.2f}\n")
        else:
            print("Produto não encontrado.\n")

    def avaliar_produto(self):
        codigo = input("Informe o código do produto que deseja avaliar: ")
        produto = self.buscar_produto(codigo)
        if produto:
            avaliacao = input("Digite sua avaliação: ")
            produto.adicionar_avaliacao(avaliacao)
            print("Avaliação adicionada com sucesso!\n")
        else:
            print("Produto não encontrado.\n")

    def menu_administrador(self):
        while True:
            print("Menu Administrador:")
            print("1. Cadastrar produto")
            print("2. Listar produtos")
            print("3. Salvar dados")
            print("4. Buscar produto")
            print("5. Excluir produto")
            print("6. Editar produto")
            print("7. Controle de estoque")
            print("8. Relatório de vendas")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                self.cadastrar_produto()
            elif opcao == '2':
                self.listar_produtos()
            elif opcao == '3':
                self.salvar_dados()
            elif opcao == '4':
                codigo = input("Informe o código do produto para busca: ")
                produto = self.buscar_produto(codigo)
                if produto:
                    print(produto)
                else:
                    print("Produto não encontrado.\n")
            elif opcao == '5':
                self.excluir_produto()
            elif opcao == '6':
                self.editar_produto()
            elif opcao == '7':
                self.controle_estoque()
            elif opcao == '8':
                self.relatorio_vendas()
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.\n")

    def menu_usuario(self):
        while True:
            print("Menu Usuário:")
            print("1. Listar produtos")
            print("2. Realizar compra")
            print("3. Buscar produto")
            print("4. Avaliar produto")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                self.listar_produtos()
            elif opcao == '2':
                self.realizar_compra()
            elif opcao == '3':
                codigo = input("Informe o código do produto para busca: ")
                produto = self.buscar_produto(codigo)
                if produto:
                    print(produto)
                else:
                    print("Produto não encontrado.\n")
            elif opcao == '4':
                self.avaliar_produto()
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.\n")

sistema = SistemaMercado()
sistema.login()