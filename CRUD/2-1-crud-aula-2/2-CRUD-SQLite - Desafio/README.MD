
# Sistema de Posts

## Tabelas

### Usuario
 - id
 - nome
 - email
 - username
 - password

### Post
 - id
 - usuario_id -> ``` Referência do usuario (foreign key)```
 - titulo
 - texto

### Comentario
 - id
 - usuario_id -> ``` Referência do usuario (foreign key) *Não Obrigatorio*```
 - post_id -> ``` Referência do post (foreign key) ```
 - texto


 ## Tabelas extras:

 ### Curtidas de Post
 ### Curtidas de Comentario
