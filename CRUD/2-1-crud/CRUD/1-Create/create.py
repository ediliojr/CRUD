class Produto(object):
    nome = None
    codigo = None
    quantidade = None
    valor = None

    def __init__(self, nome=None, codigo=None, quantidade=None, valor=None):
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade
        self.valor = valor
        
        

def create(nome=None, codigo=None, quantidade=None, valor=None):
    produto = Produto(nome, codigo, quantidade, valor) 
    return produto

def list_create(list_produto):
    # TODO: Crie um método que receba a lista de tuplas parâmetros (nome, código, quantidade, valor)
    # e retorna uma lista de objecto Produto
    list_retorno = []
    for i in list_produto:
        list_retorno.append(create(i[0],i[1],i[2],i[3]))
        
    return list_retorno
