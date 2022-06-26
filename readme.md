<h1 align="center">
 💸📦 Mercado Livre - Redis 📦💸
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

Para acessar os recursos do projeto, recomendo utilizar o Insomnia, seguindo a [documentação oficial](https://insomnia.rest/download) para sua instalação, e caso nunca tenha tido contato com essa ferramenta, [acesse este link](https://docs.insomnia.rest/insomnia/send-your-first-request).

> Depois de configurar o Insomnia, importe [esta coleção de requisições]() para consumir a API (caso tenha dúvidas de como importar, [clique aqui](https://docs.insomnia.rest/insomnia/import-export-data))

</details>

<details>
  <summary>Configurando a conexão com os bancos de dados (MongoDB e Redis)</summary>
  Para conectar com o Mongo é preciso alterar o usuário e senha no arquivo connectDb em **src/connectDb.py**.
<br><br>
 
```python
  db = pymongo.MongoClient("mongodb+srv://<user>:<password>@fa-starting-no-sql.6vnsq.mongodb.net/")
```

  Já para conectar com o Redis é preciso alterar o host, port e password no arquivo connectRedis em **src/connectRedis.py**.
<br>
 
```python
  db = redis.Redis(
      host='<host>',
      port='<port>',
      password='<password>',
      decode_responses=True
    )
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
<br>

[![image](https://img.shields.io/badge/✨%20Maria%20Gabriela%20Reis,%202022-LinkedIn-009973?style=flat-square)](https://www.linkedin.com/in/mariagabrielareis/)
