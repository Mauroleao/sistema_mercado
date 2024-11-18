from Models import *
from DAO import DaoCategoria, DaoEstoque
from datetime import datetime


class ControllerCategoria:

    def cadastrarCategoria(self, novcategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novcategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novcategoria)
            print('Categoria cadastrada com sucesso!')
        else:
            print('Categoria já existe!')


    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) == 0:
            print('Categoria não encontrada!')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso!')

        with open('categoria.txt', 'w') as arquivo:
            for i in x:
                arquivo.writelines(i.categoria)
                arquivo.writelines('\n')


    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if (x.categoria == categoriaAlterar) else (x), x))
                print('Categoria alterada com sucesso!')
            else:
                print('Categoria já existe!')
        else:
            print('Categoria não encontrada!')

        with open('categoria.txt', 'w') as arquivo:
            for i in x:
                arquivo.writelines(i.categoria)
                arquivo.writelines('\n')


    def mostrarCategorias(self):
        categoria = DaoCategoria.ler()
        if len(categoria) == 0:
            print('Nenhuma categoria cadastrada!')
        else:
            for i in categoria:
                print(f'Categoria: {i.categoria}')


class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        y = DaoCategoria.ler()
        x = DaoEstoque.ler()

        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso!')
            else:
                print('Produto já cadastrado!')
        else:
            print('Categoria não cadastrada!')


    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print('Produto removido com sucesso!')
        else:
            print('Produto não encontrado!')

        with open('estoque.txt', 'w') as arquivo:
            for i in x:
                arquivo.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arquivo.writelines('\n')    

a = ControllerEstoque()
a.removerProduto('Arroz')