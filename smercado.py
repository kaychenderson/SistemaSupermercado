class Produto:
    def __init__(self, codigo, nome, tipo, preco, setor, desconto, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.preco = preco
        self.setor = setor
        self.desconto = desconto
        self.quantidade = quantidade

    def calcular_preco_com_desconto(self):
        return self.preco * (1 - self.desconto / 100)

    def __str__(self):
        return (f"Código: {self.codigo}\n"
                f"Nome: {self.nome}\n"
                f"Tipo: {self.tipo}\n"
                f"Preço: R${self.preco:.2f}\n"
                f"Setor: {self.setor}\n"
                f"Desconto: {self.desconto}%\n"
                f"Quantidade: {self.quantidade}\n")

class Usuario:
    def __init__(self, email, senha, is_admin=False):
        self.email = email
        self.senha = senha
        self.is_admin = is_admin

class SistemaMercado:
    def __init__(self):
        self.produtos = []
        self.usuarios = {
            "admin@gmail.com": Usuario("admin@gmail.com", "admin123", is_admin=True)
        }
        self.usuario_logado = None
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
            return True
        else:
            print("Email ou senha incorretos.")
            return False

    def cadastrar_usuario(self, email, senha):
        """Cadastro de um novo usuário comum"""
        self.usuarios[email] = Usuario(email, senha)
        print("Usuário comum cadastrado com sucesso!\n")

    def cadastrar_produto(self):
        if not self.usuario_logado or not self.usuario_logado.is_admin:
            print("Permissão negada. Apenas administradores podem cadastrar produtos.")
            return

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
                if produto.quantidade < 5:
                    print("Atenção: Estoque baixo!")
                print("---------------------------")

    def realizar_compra(self):
        if not self.usuario_logado:
            print("Você precisa estar logado para realizar uma compra.")
            return

        codigo = input("Informe o código do produto que deseja comprar: ")
        quantidade_desejada = int(input("Informe a quantidade: "))

        for produto in self.produtos:
            if produto.codigo == codigo:
                if produto.quantidade < quantidade_desejada:
                    print("Estoque insuficiente.")
                    return
                
                preco_total = produto.calcular_preco_com_desconto() * quantidade_desejada
                produto.quantidade -= quantidade_desejada
                print(f"Compra realizada! Total: R${preco_total:.2f}\n")
                return

        print("Produto não encontrado.\n")

    def salvar_dados(self):
        if not self.usuario_logado or not self.usuario_logado.is_admin:
            print("Permissão negada. Apenas administradores podem salvar dados.")
            return

        with open("produtos.txt", 'w') as f:
            for produto in self.produtos:
                f.write(f"{produto.codigo},{produto.nome},{produto.tipo},{produto.preco},{produto.setor},{produto.desconto},{produto.quantidade}\n")
        print("Dados salvos com sucesso!\n")

    def carregar_dados(self):
        try:
            with open("produtos.txt", 'r') as f:
                for linha in f:
                    codigo, nome, tipo, preco, setor, desconto, quantidade = linha.strip().split(',')
                    self.produtos.append(Produto(codigo, nome, tipo, float(preco), setor, float(desconto), int(quantidade)))
            print("Dados carregados com sucesso!\n")
        except FileNotFoundError:
            print("Arquivo de produtos não encontrado. Iniciando sistema sem produtos.\n")

    def menu_administrador(self):
        while True:
            print("Menu Administrador:")
            print("1. Cadastrar produto")
            print("2. Listar produtos")
            print("3. Salvar dados")
            print("0. Sair")
            
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                self.cadastrar_produto()
            elif opcao == '2':
                self.listar_produtos()
            elif opcao == '3':
                self.salvar_dados()
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.\n")

    def menu_usuario(self):
        while True:
            print("Menu Usuário:")
            print("1. Listar produtos")
            print("2. Realizar compra")
            print("0. Sair")
            
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                self.listar_produtos()
            elif opcao == '2':
                self.realizar_compra()
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.\n")

    def iniciar(self):
        while True:
            print("Bem-vindo ao Sistema de Mercado!")
            if not self.usuario_logado:
                if not self.login():
                    continue
            
            if self.usuario_logado.is_admin:
                self.menu_administrador()
            else:
                self.menu_usuario()
            break

sistema = SistemaMercado()
sistema.iniciar()