from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arquivo:
            arquivo.writelines(categoria)
            arquivo.writelines('\n')


    @classmethod
    def ler(cls):

        with open('categoria.txt', 'r') as arquivo:
            cls.categoria = arquivo.readlines()
        
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))

        
        return cat
    
class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as arquivo:
            arquivo.writelines(venda.intensVerdido.nome + "|" + venda.intensVerdido.preco + "|" + str(venda.intensVerdido.categoria) + "|" + str(venda.vendedor) + "|" + str(venda.comprador)  + "|" + str(venda.quantidadeVendida) + "|" + str(venda.data))
            arquivo.writelines('\n')

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arquivo:
            cls.venda = arquivo.readlines()
        
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))

        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))

        return vend    


class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as arquivo:
            arquivo.writelines(produto.nome + "|" + produto.preco + "|" + produto.categoria + "|" + str(quantidade))
            arquivo.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arquivo:
            cls.estoque = arquivo.readlines()
        
        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], Categoria(i[2])), i[3]))

        return est        
    

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedor.txt', 'a') as arquivo:
            arquivo.writelines(fornecedor.nome + "|" + fornecedor.cnpj + "|" + fornecedor.telefone + "|" + fornecedor.categoria)
            arquivo.writelines('\n')


    @classmethod
    def ler(cls):
        with open('fornecedor.txt', 'r') as arquivo:
            cls.fornecedor = arquivo.readlines()
        
        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))

        forn = []
        for i in cls.fornecedor:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))

        return forn


class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'a') as arquivo:
            arquivo.writelines(pessoa.nome + "|" + pessoa.telefone + "|" + pessoa.cpf + "|" + pessoa.email + "|" + pessoa.endereco)
            arquivo.writelines('\n')


    @classmethod
    def ler(cls):
        with open('cliente.txt', 'r') as arquivo:
            cls.pessoa = arquivo.readlines()

        cls.cliente = list(map(lambda x: x.replace('\n', ''), cls.cliente))
        cls.cliente = list(map(lambda x: x.split('|'), cls.cliente))

        cliente = []
        for i in cls.cliente:
            cliente.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))

        return cliente


class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionario.txt', 'a') as arquivo:
            arquivo.writelines(funcionario.clt + "|" + funcionario.nome + "|" + funcionario.telefone + "|" + funcionario.cpf + "|" + funcionario.email + "|" + funcionario.endereco)
            arquivo.writelines('\n')


    @classmethod
    def ler(cls):
        with open('funcionario.txt', 'r') as arquivo:
            cls.funcionario = arquivo.readlines()

        cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))
        cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))

        func = []
        for i in cls.funcionario:
            func.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))

        return func            
   