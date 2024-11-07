import datetime

class Produto:
    def __init__(self, codigo, nome, tipo, preco, setor, desconto, quantidade, avaliacao=0):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.preco = preco
        self.setor = setor
        self.desconto = desconto
        self.quantidade = quantidade
        self.avaliacao = avaliacao  # Nova funcionalidade para armazenar avaliações

    def preco_final(self, imposto=0.1):
        preco_com_desconto = self.preco * (1 - self.desconto / 100)
        preco_com_imposto = preco_com_desconto * (1 + imposto)
        return preco_com_imposto

    def __str__(self):
        return (f"Código: {self.codigo}\n"
                f"Nome: {self.nome}\n"
                f"Tipo: {self.tipo}\n"
                f"Preço: R${self.preco:.2f}\n"
                f"Preço com Desconto e Imposto: R${self.preco_final():.2f}\n"
                f"Setor: {self.setor}\n"
                f"Desconto: {self.desconto}%\n"
                f"Quantidade: {self.quantidade}\n"
                f"Avaliação: {self.avaliacao}/5\n")

class SistemaMercado:
    def __init__(self):
        self.produtos = []
        self.vendas = []

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
                produto.nome = input("Informe o novo nome: ")
                produto.tipo = input("Informe o novo tipo: ")
                produto.preco = float(input("Informe o novo preço: "))
                produto.setor = input("Informe o novo setor: ")
                produto.desconto = float(input("Informe o novo desconto (em %): "))
                produto.quantidade = int(input("Informe a nova quantidade em estoque: "))
                print("Produto editado com sucesso!\n")
                return
        print("Produto não encontrado.\n")

    def controle_estoque(self):
        minimo_estoque = int(input("Informe a quantidade mínima para alerta: "))
        for produto in self.produtos:
            if produto.quantidade < minimo_estoque:
                print(f"Alerta: Estoque baixo para o produto {produto.nome}, quantidade: {produto.quantidade}")
                if input("Deseja repor o estoque automaticamente? (s/n): ").lower() == 's':
                    produto.quantidade = minimo_estoque
                    print(f"O estoque do produto {produto.nome} foi atualizado para {minimo_estoque}\n")

    def realizar_venda(self):
        codigo = input("Informe o código do produto para vender: ")
        quantidade = int(input("Informe a quantidade para venda: "))
        for produto in self.produtos:
            if produto.codigo == codigo:
                if produto.quantidade >= quantidade:
                    produto.quantidade -= quantidade
                    valor_venda = produto.preco_final() * quantidade
                    self.vendas.append((produto, quantidade, valor_venda, datetime.datetime.now()))
                    print(f"Venda realizada com sucesso! Valor total: R${valor_venda:.2f}")
                    return
                else:
                    print("Erro: Quantidade insuficiente em estoque.")
                    return
        print("Produto não encontrado.\n")

    def relatorio_vendas(self):
        print("Relatório de Vendas:")
        total_vendas = 0
        for venda in self.vendas:
            produto, quantidade, valor_venda, data = venda
            print(f"{data}: Produto {produto.nome}, Quantidade {quantidade}, Valor: R${valor_venda:.2f}")
            total_vendas += valor_venda
        print(f"Total vendido: R${total_vendas:.2f}\n")

    def avaliar_produto(self):
        codigo = input("Informe o código do produto para avaliar: ")
        for produto in self.produtos:
            if produto.codigo == codigo:
                avaliacao = int(input("Dê uma nota de 1 a 5 para o produto: "))
                if 1 <= avaliacao <= 5:
                    produto.avaliacao = avaliacao
                    print(f"Produto {produto.nome} avaliado com sucesso!\n")
                else:
                    print("Erro: Avaliação inválida.")
                return
        print("Produto não encontrado.\n")

    def salvar_dados(self, arquivo="produtos.txt"):
        with open(arquivo, 'w') as f:
            for produto in self.produtos:
                f.write(f"{produto.codigo},{produto.nome},{produto.tipo},{produto.preco},{produto.setor},{produto.desconto},{produto.quantidade},{produto.avaliacao}\n")
        print("Dados salvos com sucesso!\n")

    def carregar_dados(self, arquivo="produtos.txt"):
        try:
            with open(arquivo, 'r') as f:
                for linha in f:
                    codigo, nome, tipo, preco, setor, desconto, quantidade, avaliacao = linha.strip().split(',')
                    self.produtos.append(Produto(codigo, nome, tipo, float(preco), setor, float(desconto), int(quantidade), int(avaliacao)))
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
    print("6. Controle de Estoque")
    print("7. Realizar Venda")
    print("8. Relatório de Vendas")
    print("9. Avaliar Produto")
    print("10. Salvar dados")
    print("11. Carregar dados")
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
        sistema.controle_estoque()
    elif opcao == '7':
        sistema.realizar_venda()
    elif opcao == '8':
        sistema.relatorio_vendas()
    elif opcao == '9':
        sistema.avaliar_produto()
    elif opcao == '10':
        sistema.salvar_dados()
    elif opcao == '11':
        sistema.carregar_dados()
    elif opcao == '0':
        print("Encerrando o sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
