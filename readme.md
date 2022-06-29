<h1 align="center">
 💸📦 Mercado Livre - Cassandra 📦💸
</h1>

<p align="center">
  <a href="#projeto">Sobre o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#requisitos">Como rodar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#demo">Demonstração</a>
</p>

<span id="projeto">
  
# :bookmark_tabs: Sobre o projeto
Este é um sistema que visa realizar opreações de CRUD a partir de um modelo de dados não relacional criado baseando-se nas transações do Mercado Livre (de maneira simplificada), assim servindo como prática de conexão com bancos de dados não relacionais como MongoDB, Redis e Cassandra.

> - 💡 Atividade 1: modelar de forma relacional e não relacional uma biblioteca e o mercado livre
> - 💡 Atividade 2: implementar as modelagens não relacionais da biblioteca e do mercado livre no MongoDB
> - 💡 Atividade 3: manipular documentos do MongoDB utilizando Python
> - 💡 Atividade 4: manipular documentos Chave-Valor no Redis utilizando Python
> - 💡 Atividade 5: manipular dados no Cassandra utilizando Python

<span id="requisitos">

# :gear: Como rodar

<details>
  <summary>Instalação de ferramentas e configuração do ambiente</summary>
  Para executar o projeto é preciso que o Python e o Git estejam instalados, além de mais algumas configurações para o uso do Flask, MongoDB, Redis e Cassandra. Para configurar o ambiente virtual, siga o tutorial abaixo:
<br><br>
 
```bash
# Verifique se o pip está instalado
python -m pip --version

# Caso não tenha instalado, acesse a  documentação oficial em: https://pip.pypa.io/en/stable/installing/

# Instale o virtualenv (ferramenta para criar ambientes Python isolados)
python -m pip install virtualenv

# Clone o repositório
git clone https://github.com/MariaGabrielaReis/BDNR-mercado-livre

# Acesse a pasta
cd BDNR-mercado-livre

# Configure o ambiente
python -m venv venv
```

Para ativar o ambiente virtual no Windows, pelo PowerShell, rode `venv\Scripts\activate`, já pelo Linux use `. venv/bin/activate`. Assim que ativado o ambiente, instale as dependências do projeto rodando o seguinte comando pelo terminal:
<br
 
```bash
pip install -r requirements.txt
```

Para acessar os recursos do projeto pode-se utilizar o Insomnia ou Postman, por exemplo.

</details>

<details>
  <summary>Configurando a conexão com os bancos de dados (MongoDB, Redis e Cassandra)</summary>
  Para conectar com o Mongo é preciso alterar o usuário e senha no arquivo connectDatabase em **src/connectDatabase.py**.
<br><br>
 
```python
  db = pymongo.MongoClient("mongodb+srv://<user>:<password>@fa-starting-no-sql.6vnsq.mongodb.net/")
```

  Já para conectar com o Redis é preciso alterar o host, port e password no arquivo connectDatabase em **src/connectDatabase.py**
<br>
 
```python
  db = redis.Redis(
      host='<host>',
      port='<port>',
      password='<password>',
      decode_responses=True
    )
```

 Por fim, para conectar com o Cassandra é preciso alterar o usuário e a senha connectDatabase em **src/connectDatabase.py**
<br>
 
```python
  auth_provider = PlainTextAuthProvider('<user>', '<password>')
```

</details>

<details>
  <summary>Rodando o Flask </summary>
  Com o ambiente virtual ativado ...
<br><br>
 
```bash
python main.py
```

O servidor inciará localmente na porta 5000. Utilize o Insomnia ou o Postman para simular requisições e respostas das rotas (pelo link [https://localhost:5000](https://localhost:5000)).

</details>

<span id="demo">
  
# :desktop_computer: Demonstração  
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
<br>

[![image](https://img.shields.io/badge/✨%20Maria%20Gabriela%20Reis,%202022-LinkedIn-009973?style=flat-square)](https://www.linkedin.com/in/mariagabrielareis/)
