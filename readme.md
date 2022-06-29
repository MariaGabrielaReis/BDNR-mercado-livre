<h1 align="center">
 💸📦 Mercado Livre 📦💸
</h1>

### :bookmark_tabs: Sobre o projeto
Este é um sistema que visa realizar opreações de CRUD a partir de um modelo de dados não relacional criado baseando-se nas transações do Mercado Livre (de maneira simplificada), assim servindo como prática de conexão com bancos de dados não relacionais como MongoDB, Redis e Cassandra.

> - 💡 Atividade 1: modelar de forma relacional e não relacional uma biblioteca e o mercado livre
> - 💡 Atividade 2: implementar as modelagens não relacionais da biblioteca e do mercado livre no MongoDB
> - 💡 Atividade 3: manipular documentos do MongoDB utilizando Python
> - 💡 Atividade 4: manipular documentos Chave-Valor no Redis utilizando Python
> - 💡 Atividade 5: manipular dados no Cassandra utilizando Python
<br>

---

### :desktop_computer: Demonstração  
Abrindo cada um dos tópicos a seguir é possível observar as entregas feitas para cada atividade:

<details>
 <summary>Atividade 1</summary>
 
 O resultado desta atividade pode ser conferido através [deste PDF](https://github.com/MariaGabrielaReis/BDNR-mercado-livre/files/9013373/20-03_exercicio_1.pdf)
</details>
 
<details>
 <summary>Atividade 2</summary>
 
 O resultado desta atividade pode ser conferido através [deste PDF](https://github.com/MariaGabrielaReis/BDNR-mercado-livre/files/9013344/27-03_exercicio_2.pdf)
</details>
 
<details>
 <summary>Atividade 3</summary>
 
 A seguir é possível conferir prints do resultado das manipulações no MongoDB para cada documento criado (através do site [https://www.mongodb.com/](https://www.mongodb.com/pt-br)):

| Usuário | ![](https://user-images.githubusercontent.com/69374340/175344828-8a604502-2734-47ed-b27d-a9ec83706380.png) |
|:--------|:-----------------------------------------------------------------------------------------------------------|
| Produto | ![](https://user-images.githubusercontent.com/69374340/175343751-7b39071b-17c4-414a-9ccb-f1f41af3f712.png) ![](https://user-images.githubusercontent.com/69374340/175343860-dab93fc3-9cb6-4f72-b5af-5cae6cdbcb4c.png) |
| Compra  | ![](https://user-images.githubusercontent.com/69374340/175343512-9e8d6f1b-2db6-449c-82d6-6412d6f1b190.png) |
</details>
 
<details>
 <summary>Atividade 4</b></summary>
 
 Para esta atividade 4, depois da criação de CRUD de usuários, produtos e compras, pensando na aplicabilidade do Redis e que em e-commerces eu, pessoalmente, utilizo muito da funcionalidade de lista de desejos, acabei agregando este recurso também a este projeto. Abaixo é possível ver o código que trás do MongoDB a lista de desejos de um determinado usuário (identificado pelo seu CPF) e cadastrando no Redis com o identificador `wishlist:<CPF do usuário>`.
 
```python
def addWishlistToRedis(params):
  userCpf = params.get("userCpf")
  user = userCollection.find_one({ "cpf": userCpf })
  redis.set(f'wishlist:{userCpf}', user['wishlist'])

  return json.dumps({"status": "ok"}) 
```
 
Já no trecho abaixo é possível resgatar o que foi cadastrado no Redis, também necessitando da passagem do CPF do usuário por parâmetro para realização da busca:
 
```python
def showRedisWishlist(params):
  userCpf = params.get("userCpf")  

  try:
    return json.loads(redis.get(f'wishlist:{userCpf}'))
  except:
    return json.dumps({"hasError": True, "Message": "Lista de desejos não encontrada!"})
```
 
E por fim, há também um recurso para deletar uma coleção do Redis se necessário:

```python
def deleteWishlistFromRedis(params):
  userCpf = params.get("userCpf")
  redis.delete(f'wishlist:{userCpf}')

  return json.dumps({"status": "OK"}) 
``` 
</details>

<details>
 <summary>Atividade 5</b></summary>
 
 Para esta atividade 5, depois da criação de CRUD de usuários, produtos e compras utilizando Mongo e a criação da funcionalidade de lista de desejos com o Redis, agora é possível obter esses dados do Redis e cadastrá-los no Cassandra, consumindo as seguintes funções:
 
 - Para adicionar a lista de desejos ao Cassandra precisamos que o CPF do usuário dono da wishlist seja passado por parâmetro para a função, que vai buscar os dados no Redis e depois executar uma query para cadastrar tais dados no Cassandra:
 
```python
def addWishlistToCassandra(params):
  userCpf = params.get("userCpf")
  redisWishlist = redis.get(f'wishlist:{userCpf}')

  cassandra.execute(f'INSERT INTO mercadolivre.wishlist (userCpf, products) VALUES ({userCpf}, {str(redisWishlist)})')

  return json.dumps({"status": "OK"})
```
 - Já no trecho abaixo é possível resgatar o que foi cadastrado no Cassandra, também necessitando da passagem do CPF do usuário por parâmetro para realização da busca:
 
```python
def showCassandraWishlist(params):
  userCpf = params.get("userCpf")
  response = cassandra.execute(f'SELECT * FROM mercadolivre.wishlist WHERE userCpf = {userCpf}')
  
  if (not response):
    return json.dumps({"hasError": True, "Message": "Lista de desejos não encontrada!"})

  response = response[0]
  return json.dumps({
    "userCpf": response.userCpf,
    "products": json.dumps({response.products})
  })
```
 
- E por fim, há também um recurso para deletar os dados cadastrados no Cassandra se necessário, também recorrendo ao uso do CPF do usuário:

```python
def deleteWishlistFromCassandra(params):
  userCpf = params.get("userCpf")
  cassandra.execute(f'DELETE FROM mercadolivre.wishlist WHERE userCpf = {userCpf} IF EXISTS')

  return json.dumps({"status": "OK"}) 
``` 
</details>

<br>

[![image](https://img.shields.io/badge/✨%20Maria%20Gabriela%20Reis,%202022-LinkedIn-009973?style=flat-square)](https://www.linkedin.com/in/mariagabrielareis/)
