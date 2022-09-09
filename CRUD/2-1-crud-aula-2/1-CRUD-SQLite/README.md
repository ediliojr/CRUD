## Tabela de movimentações financeira

### Colunas da Tabela
 - id
 - data
 - nome
 - tipo (saida ou entrada)
 - valor

### Metodos
 - create_table -> ``` Cria a tabela ```
 - insert -> ``` Insere dados na tabela ```
 - select -> ``` Seleciona um linha da tabela ```
 - select_list -> ``` Seleciona varias linhas da tabela ```
 - update -> ``` Atualiza uma ou mais coluna da linha  da tabela *(Um item por vez)*```
 - delete -> ``` Deleta um item da tabela *(Um item por vez)* ```
 - entradas -> ``` Seleciona e retorna o total de entradas ```
 - saidas -> ``` Seleciona e retorna o total de saidas ```

 #### Metodos extras:
 - maior valor de entrada
 - menor valor de entrada
 - maior valor de saida
 - menor valor de saida
 - saldo (entradas - saidas)



 ### Obs: **Nao esqueça de inicializar o sqlite**
