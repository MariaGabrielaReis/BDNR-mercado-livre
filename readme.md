<h1 align="center">
 💸📦 Mercado Livre 📦💸
</h1>

<p align="center">
  <a href="#projeto">Sobre o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#requisitos">Como rodar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#demo">Demonstração</a>
</p>

<span id="projeto">
  
# :bookmark_tabs: Sobre o projeto
Este é um sistema que visa realizar opreações de CRUD a partir de um modelo de dados não relacional criado baseando-se nas transações do Mercado Livre (de maneira simplificada), assim servindo como prática de conexão com bancos de dados não relacionais como MongoDB, Redis e Cassandra.

> - 💡 Atividade 1: ...
> - 💡 Atividade 2: ...
> - 💡 Atividade 3: manipular documentos do MongoDB utilizando Python (CRUD de documentos)
> - 💡 Atividade 4: manipular documentos Chave-Valor no Redis utilizando Python
> - 💡 Atividade 5: manipular dados no Cassandra utilizando Python

<span id="requisitos">

# :gear: Como rodar

<details>
  <summary>Instalação de ferramentas e configuração do ambiente</summary>
  <br>
  Para executar o projeto é preciso que o Python e o Git estejam instalados, além de mais algumas configurações para o uso do Flask, MongoDB, Redis e Cassandra. Para configurar o ambiente virtual, siga o tutorial abaixo:

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

```bash
pip install -r requirements.txt
```

Para acessar os recursos do projeto, recomendo utilizar o Insomnia, seguindo a [documentação oficial](https://insomnia.rest/download) para sua instalação, e caso nunca tenha tido contato com essa ferramenta, [acesse este link](https://docs.insomnia.rest/insomnia/send-your-first-request).

> Depois de configurar o Insomnia, importe [esta coleção de requisições]() para consumir a API (caso tenha dúvidas de como importar, [clique aqui](https://docs.insomnia.rest/insomnia/import-export-data))

</details>

<details>
  <summary>Configurando a conexão com os bancos de dados</summary>
  <br>

<details>
  <summary>MongoDB</summary>
  <br>
  Para conectar com o Mongo é preciso alterar o usuário e senha no arquivo connectDb em **src/connectDb.py**.

```python
  db = pymongo.MongoClient("mongodb+srv://<user>:<password>@fa-starting-no-sql.6vnsq.mongodb.net/")
```

</details>

<details>
  <summary>Redis </summary>
  <br>
  Para conectar com o Redis é preciso alterar o host, port e password no arquivo connectRedis em **src/connectRedis.py**.

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
  <summary>Cassandra</summary>
  <br>
  Para conectar com o Cassandra é preciso alterar o ASTRA_DB_ID, ASTRA_DB_REGION e ASTRA_DB_APPLICATION_TOKEN no arquivo connectCassandra em **src/connectCassandra.py**.

```python
  ASTRA_DB_ID = '<BD-ID>'
  ASTRA_DB_REGION = '<DB-REGION>'
  ASTRA_DB_APPLICATION_TOKEN = '<token>'
  ASTRA_DB_KEYSPACE = 'mercadolivre'
  TEST_COLLECTION_NAME = "test"
```

</details>

</details>

<details>
  <summary>Rodando o Flask </summary>
  <br>
  Com o ambiente virtual ativado ...

```bash
python main.py
```

O servidor inciará localmente na porta 5000. Utilize o Insomnia ou o Postman para simular requisições e respostas das rotas (pelo link [https://localhost:5000](https://localhost:5000)).

</details>

<span id="demo">
  
# :desktop_computer: Demonstração  
Abrindo cada um dos tópicos a seguir é possível observar as entregas feitas para cada atividade:

<details>
 <summary>Atividade 1</summary>
 <br>
 Em breve!
</details>
 
<details>
 <summary>Atividade 2</summary>
 <br>
 Em breve!
</details>
 
<details>
 <summary>Atividade 3</summary>
 <br>

Intruções:

```bash
1 - pip install pymongo
2 - pip install dnspython
```

```python
import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb+srv://mane:124578895623@branco.3nl94.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

global mydb
mydb = client.mercadolivre

# criar funções de CRUD
```

</details>
 
<details>
 <summary>Atividade 4</b></summary>
 <br>
Baseado no Modelo Não Relacional criado, selecionar quais coleções podem ser armazenadas no Redis a fim de aumentar a performance do sistema e facilitar a operação das funcionalidades. Novas funcionalidades também podem ser sugeridas.
> Implementação no Python do acesso ao Redis para inserção, consulta e deleção das chave
</details>

<details>
 <summary>Atividade 5</b></summary>
 <br>
 Recuperar os dados temporários no Redis e inserir no Cassandra
</details>

<br>

[![image](https://img.shields.io/badge/✨%20Maria%20Gabriela%20Reis,%202022-LinkedIn-009973?style=flat-square)](https://www.linkedin.com/in/mariagabrielareis/)
