from produto import Produto

class ListaDeProdutos:
    """
    Teste de DOC - Depende de outro componente para ser testado, no caso ele depende do Produto
    """
    def __init__(self) -> None:
        """
        Este construtor sera utilizado para armazenar objetos do tipo Produto"""
        self.produtos: list[Produto] = [] # Inicializa uma lista vazia
        self.contador_de_id = 1


    def cria_produto(self, marca, codigo, preco_unitario, quantidade: int = 0) -> Produto:
        """Cria e adiciona um produto à lista."""
        produto = Produto(
            self.contador_de_id, 
            marca,
            codigo, 
            preco_unitario, 
            quantidade
        )
        self.produtos.append(produto)
        self.contador_de_id += 1
        return produto

    def atualizar_produto(
        self,
        identificador: int,
        codigo: int | None = None,
        marca: str | None = None,
        preco_unitario: float | None = None,
        quantidade: int | None = None
    ) -> None:
        """Atualiza os atributos de um produto, com validação."""
        for produto in self.produtos:
            if produto.id == identificador:
                # Validação de entrada
                if codigo is not None:
                    if not isinstance(codigo, int) or codigo <= 0:
                        raise ValueError("Código deve ser um número inteiro positivo.")
                    produto.codigo = codigo

                if marca is not None:
                    if not isinstance(marca, str) or not marca.strip():
                        raise ValueError("Marca deve ser uma string não vazia.")
                    produto.marca = marca

                if preco_unitario is not None:
                    if preco_unitario <= 0:
                        raise ValueError("Preço unitário deve ser maior que zero.")
                    produto.preco_unitario = preco_unitario

                if quantidade is not None:
                    if quantidade < 0:
                        raise ValueError("Quantidade não pode ser negativa.")
                    produto.quantidade = quantidade

                break

    def deletar_produto(self, identificador: int) -> None:
        """Remove um produto da lista pelo ID."""
        produto_encontrado = None
        for produto in self.produtos:
            if produto.id == identificador:
                produto_encontrado = produto
                break
        
        if produto_encontrado:
            self.produtos.remove(produto_encontrado)
        else:
            raise ValueError(f"Produto com ID {identificador} não encontrado na lista.")


    def recuperar_produto(self, identificador: int) -> Produto | None:
        """Recupera um produto pelo ID. """
        for produto in self.produtos:
            if produto.id == identificador:
                return produto
        return None

    def listar_produtos(self) -> None:
        """Exibe todos os produtos cadastrados."""
        for produto in self.produtos:
            print(produto)
        