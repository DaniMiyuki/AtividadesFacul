# Teste de SCHEMA

from produto import Produto

def test_schema_produto():
    # Tentativa de criar uma instância da classe Produto
    produto = Produto(
        id=1,
        codigo=123456,
        marca="Goodyear",
        quantidade=10,
        preco_unitario=450.0
    )
    # Verifica se os atributos estão presentes e com os tipos corretos
    assert isinstance(produto.id, int), "O atributo 'id' deve ser do tipo int"
    assert isinstance(produto.codigo, int), "O atributo 'codigo' deve ser do tipo int"
    assert isinstance(produto.marca, str), "O atributo 'marca' deve ser do tipo str"
    assert isinstance(produto.quantidade, int), "O atributo 'quantidade' deve ser do tipo int"
    assert isinstance(produto.preco_unitario, float), "O atributo 'valor_unitario' deve ser do tipo float"


# Teste de DOC

from produto import Produto
from lista_de_produtos import ListaDeProdutos

def test_criar_produto():
    lista = ListaDeProdutos()
    produto = lista.cria_produto( 123456, "Goodyear", 10, 100.0)

    assert produto.id == 1, "O ID do produto deve ser 1"
    assert produto.codigo == 123456, "O código do produto deve ser 123456"
    assert produto.marca == "Goodyear", "A marca do produto deve ser 'Goodyear'"    
    assert produto.quantidade == 10, "A quantidade do produto deve ser 10"
    assert produto.preco_unitario == 100.0, "O preço unitário do produto deve ser 100.0"

def test_atualizar_produto_codigo_invalido():
    lista = ListaDeProdutos()
    produto = lista.cria_produto(codigo=123456, marca="Goodyear", preco_unitario=100.0, quantidade=10)

    try:
        lista.atualizar_produto(identificador=produto.id, codigo=-654321)
        assert False, "Deveria ter lançado um ValueError para código negativo."
    except ValueError as e:
        assert str(e) == "Código deve ser um número inteiro positivo.", f"Mensagem de erro incorreta: {e}"

    try:
        lista.atualizar_produto(identificador=produto.id, marca="")
        assert False, "Deveria ter lançado um ValueError para marca vazia."
    except ValueError as e:
        assert str(e) == "Marca deve ser uma string não vazia.", f"Mensagem de erro incorreta: {e}"

    try:
        lista.atualizar_produto(identificador=produto.id, preco_unitario=-100.0)
        assert False, "Deveria ter lançado um ValueError para preço unitário negativo."
    except ValueError as e:
        assert str(e) == "Preço unitário deve ser maior que zero.", f"Mensagem de erro incorreta: {e}"
    
    try:
        lista.atualizar_produto(identificador=produto.id, quantidade=-1)
        assert False, "Deveria ter lançado um ValueError para quantidade negativa."
    except ValueError as e:
        assert str(e) == "Quantidade não pode ser negativa.", f"Mensagem de erro incorreta: {e}"
    
    
    # Atualização válida
    lista.atualizar_produto(identificador=produto.id, codigo=654321, marca="Firestone", preco_unitario=120.0, quantidade=15)

    # Verificação da atualização
    assert produto.codigo == 654321, "O código do produto deve ser atualizado corretamente"
    assert produto.marca == "Firestone", "A marca do produto deve ser atualizada corretamente"
    assert produto.preco_unitario == 120.0, "O preço unitário do produto deve ser atualizado corretamente"
    assert produto.quantidade == 15, "A quantidade do produto deve ser atualizada corretamente"

def test_deletar_produto():
    lista = ListaDeProdutos()
    produto = lista.cria_produto(codigo=123456, marca="Goodyear", preco_unitario=100.0, quantidade=10)
    
    lista.deletar_produto(produto.id)

    # Verificar se o produto foi realmente removido
    produto_removido = lista.recuperar_produto(produto.id)
    assert produto_removido is None, f"O produto com ID {produto.id} deveria ter sido removido da lista."

def test_recuperar_produto():
    lista = ListaDeProdutos()
    produto = lista.cria_produto(codigo=123456, marca="Goodyear", preco_unitario=100.0, quantidade=10)
    produto_recuperado = lista.recuperar_produto(produto.id)

    assert produto_recuperado == produto, "O produto recuperado deve ser o mesmo que foi criado"

def test_listar_produtos():
    lista = ListaDeProdutos()
    lista.cria_produto("Produto 1", 100.0, 10)
    lista.cria_produto("Produto 2", 150.0, 5)

    # Testa se o número de produtos na lista é 2
    assert len(lista.produtos) == 2, "Deve haver 2 produtos na lista"