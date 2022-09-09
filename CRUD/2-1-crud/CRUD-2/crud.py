class Compras(object):
    # TODO: Crear um Objeto modelo para fazer as operaçoes do CRUD
    # TODO: O objeto modelo referencia para registros de compras
    # TODO: As informaçoes a ser gardadas são:
    # TODO: Um identificador unico (id)  data da compra, valor da compra, item comprado,
    # quantidade e nome de quem comprou para cada compra realizada
    
    
    def __init__(self,identificador=None,data=None,valor=None,item=None,quantidade=None,nome_comprador=None):
        self.identificador = identificador
        self.data = data
        self.valor = valor
        self.item = item
        self.nome_comprador = nome_comprador
        self.quantidade = quantidade

ind_prox = 1
lista_compras = []

def create(data=None,valor=None,item=None,quantidade=None,nome_comprador=None):
    # TODO: Crear metodo, onde receba os valores do modelo, crie um objeto
    #  Adicione na lista "MEMORY", e retornar o objeto 
    lista_compras.append(ind_prox,data,valor,item,quantidade,nome_comprador)
    ind_prox +=1

def update(identificador,data=None,valor=None,item=None,quantidade=None,nome_comprador=None):
    # TODO: Implemte a atualizaçao do objeto, tendo em  vista que pode-se passar todos as propriedades ou só uma
    # TODO: Recebe o objeto e os valores
    # TODO: Lembre que o indentificador não pode-se editar
    for i in lista_compras:
        if i.indentificador == identificador:
            if data:
                i.data = data
            if valor:
                i.valor = valor
            if item:
                i.item = item
            if quantidade:
                i.quantidade = quantidade
            if nome_comprador:
                i.nome_comprador = nome_comprador
    

def read():
    # TODO: Implementado o retorno das propriedaedes e valores em um dicionario,
    # retorne o metodo que tras os valores do objeto
    # OBS: implemente tambem uma tabela de retorno
    
    for i in lista_compras:
        print(f"| {i.indentificador} | {i.data}| {i.item} |{i.quantidade} |{i.valor} | {i.nome_comprador}")

def delete(identificador):
    # TODO: Delete o objeto e retorne um booleando True para indicar que a operação foi feita
    for i in lista_compras:
        if i.indentificador == identificador:
            lista_compras.remove(i)