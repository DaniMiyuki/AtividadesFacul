from dataclasses import dataclass

class Cliente:
    def __init__(self, id, nome, cpf, email, contato, endereco, historico_compras, devolucoes_trocas):
        id: int
        nome: str
        email: str
        contato: str
        endereco: str
        historico_compras: list
        devolucoes_trocas: list

    def test_atualizar_produto():
    lista = ListaDeProdutos()
    produto = lista.cria_produto("Produto 1", 100.0, 10)
    lista.atualizar_produto(produto.id, nome="Produto Atualizado", preco_unitario=120.0, quantidade=15)

    assert produto.nome == "Produto Atualizado", "O nome do produto deve ser atualizado"
    assert produto.preco_unitario == 120.0, "O preço unitário do produto deve ser atualizado"
    assert produto.quantidade == 15, "A quantidade do produto deve ser atualizada"

def test_deletar_produto():
    lista = ListaDeProdutos()
    produto = lista.cria_produto("Produto 1", 100.0, 10)
    lista.deletar_produto(produto.id)

    assert lista.recuperar_produto(produto.id) is None, "O produto deveria ter sido removido da lista"

def test_recuperar_produto():
    lista = ListaDeProdutos()
    produto = lista.cria_produto("Produto 1", 100.0, 10)
    produto_recuperado = lista.recuperar_produto(produto.id)

    assert produto_recuperado == produto, "O produto recuperado deve ser o mesmo que foi criado"

def test_listar_produtos():
    lista = ListaDeProdutos()
    lista.cria_produto("Produto 1", 100.0, 10)
    lista.cria_produto("Produto 2", 150.0, 5)

    # Testa se o número de produtos na lista é 2
    assert len(lista.produtos) == 2, "Deve haver 2 produtos na lista"    