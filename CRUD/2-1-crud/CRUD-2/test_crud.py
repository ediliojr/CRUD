from crud import (
    Compras,
    create,
    update,
    read,
    delete
    )
import inspect
import pytest
#valores 
DATA = "12/01/2022"
VALOR = 3.12
ITEM  = "Bolacha"
QUANT = 2
NOME = "Gabriel"
ID = 1
NEW_VALOR = 4

def test_class_corret():
    assert hasattr(Compras, 'identificador') == True, "Objeto nao tem propriedade 'identificador'"
    assert hasattr(Compras, 'data') == True, "Objeto nao tem propriedade 'data'"
    assert hasattr(Compras, 'valor') == True, "Objeto nao tem propriedade 'valor'"
    assert hasattr(Compras, 'item') == True, "Objeto nao tem propriedade 'item'"
    assert hasattr(Compras, 'quantidade') == True, "Objeto nao tem propriedade 'quantidade'"
    assert hasattr(Compras, 'nome_comprador') == True, "Objeto nao tem propriedade 'nome_comprador'"

def test_parameters():
  assert len(inspect.getfullargspec(create).args) == 6, "Assinatura da função deverá receber 6 parâmetros"
  assert len(inspect.getfullargspec(update).args) == 6, "Assinatura da função deverá receber 6 parâmetros"
  assert len(inspect.getfullargspec(read).args) == 1, "Assinatura da função deverá receber 1 parâmetros"
  assert len(inspect.getfullargspec(delete).args) == 1, "Assinatura da função deverá receber 1 parâmetros"

def test_not_none():
    assert Compras is not None , "Esperado valor diferente de 'None'"
    assert create(ID,DATA,VALOR,ITEM,QUANT,NOME) is not None, f"Esperado valor diferente de 'None'"
    upda = create(ID,DATA,VALOR,ITEM,QUANT,NOME)
    assert update(upda,DATA,NEW_VALOR,ITEM,QUANT,NOME) is not None, f"Esperado valor diferente de 'None'"
    assert read(upda) is not None, f"Esperado valor diferente de 'None'"
    assert delete(upda) is not None, f"Esperado valor diferente de 'None'"
    
    #assert other_multiplication_table(3) is not None, "Esperado valor diferente de 'None'"
    
def test_type():
    ct = create(ID,DATA,VALOR,ITEM,QUANT,NOME)
    assert type(ct) is Compras, "Esperado objeto do type <'class' Compras>"
    assert type(update(ct,DATA,NEW_VALOR,ITEM,QUANT,NOME)) is Compras, "Esperado objeto do type <'class' Compras>"
    assert type(read(ct)) is dict, "Esperado objeto do type <'dict'>"
    assert type(delete(ct)) is bool, "Esperado objeto do type None"

@pytest.mark.parametrize("identificador,data,valor,item,quantidade,nome_comprador, expectativa",[
    (1,"12/11/2021",3.1,"bombons",13,"Leandro",Compras(1,"12/11/2021",3.1,"bombons",13,"Leandro")),
    (2,"21/01/2022",14.7,"Chocolate",1,"Ana",Compras(2,"21/01/2022",14.7,"Chocolate",1,"Ana")),    
])
def test_create(identificador,data,valor,item,quantidade,nome_comprador,expectativa):
    cret = create(identificador,data,valor,item,quantidade,nome_comprador)
    assert cret.identificador == expectativa.identificador, f"'id' esperado não retornado"
    assert cret.data == expectativa.data, "'data' esperado não retornado"
    assert cret.valor == expectativa.valor, "'valor' esperado não retornado"
    assert cret.item == expectativa.item, "'item' esperado não retornado"
    assert cret.quantidade == expectativa.quantidade, "'quantidade' esperado não retornado"
    assert cret.nome_comprador == expectativa.nome_comprador, "'nome_comprador' esperado não retornado"

@pytest.mark.parametrize(
    "identificador, data, valor, item, quantidade, nome_comprador, expectativa, \
    new_data, new_valor, new_item, new_quantidade, new_nome_comprador, new_expectativa",[
    (1,"12/11/2021",3.1,"bombons",13,"Leandro",Compras(1,"12/11/2021",3.1,"bombons",13,"Leandro"),
    "21/01/2022",14.7,"Chocolate",1,"Ana",Compras(1,"21/01/2022",14.7,"Chocolate",1,"Ana")
     
    ),
    (2,"21/01/2022",14.7,"Chocolate",1,"Ana",Compras(2,"21/01/2022",14.7,"Chocolate",1,"Ana"),
     "12/11/2021",3.1,"bombons",13,"Leandro",Compras(2,"12/11/2021",3.1,"bombons",13,"Leandro")
    ),    
])
def test_update(identificador, data, valor, item, quantidade, nome_comprador, expectativa,
    new_data, new_valor, new_item, new_quantidade, new_nome_comprador, new_expectativa
    ):
    cret = create(identificador,data,valor,item,quantidade,nome_comprador)
    assert cret.identificador == expectativa.identificador, f"'id' esperado não retornado"
    assert cret.data == expectativa.data, "'data' esperado não retornado"
    assert cret.valor == expectativa.valor, "'valor' esperado não retornado"
    assert cret.item == expectativa.item, "'item' esperado não retornado"
    assert cret.quantidade == expectativa.quantidade, "'quantidade' esperado não retornado"
    assert cret.nome_comprador == expectativa.nome_comprador, "'nome_comprador' esperado não retonado"
    
    upt = update(cret,new_data, new_valor, new_item, new_quantidade, new_nome_comprador)
    assert upt.identificador == new_expectativa.identificador, f"'id' esperado não retornado"
    assert upt.data == new_expectativa.data, "'data' esperado não retornado"
    assert upt.valor == new_expectativa.valor, "'valor' esperado não retornado"
    assert upt.item == new_expectativa.item, "'item' esperado não retornado"
    assert upt.quantidade == new_expectativa.quantidade, "'quantidade' esperado não retornado"
    assert upt.nome_comprador == new_expectativa.nome_comprador, "'nome_comprador' esperado não retonado"
    
@pytest.mark.parametrize("expectativa",[
    (Compras(1,"12/11/2021",3.1,"bombons",13,"Leandro")),
    (Compras(2,"21/01/2022",14.7,"Chocolate",1,"Ana")),    
])    
def test_read(expectativa):
    rd_c = read(expectativa)
    assert rd_c["identificador"] == expectativa.identificador, "Espera o dado 'identificador' no dicionario"
    assert rd_c["data"] == expectativa.data, "Espera o dado 'data' no dicionario"
    assert rd_c["valor"] == expectativa.valor, "Espera o dado 'valor' no dicionario"
    assert rd_c["item"] == expectativa.item, "Espera o dado 'item' no dicionario"
    assert rd_c["quantidade"] == expectativa.quantidade, "Espera o dado 'quantidade' no dicionario"
    assert rd_c["nome_comprador"] == expectativa.nome_comprador, "Espera o dado 'nome_comprador' no dicionario"
    
@pytest.mark.parametrize("expectativa",[
    (Compras(1,"12/11/2021",3.1,"bombons",13,"Leandro")),
    (Compras(2,"21/01/2022",14.7,"Chocolate",1,"Ana")),    
])    
def test_delete(expectativa):
    assert delete(expectativa) == True, "Espera um valor booleano"