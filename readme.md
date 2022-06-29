<h1 align="center">
 💸📦 Mercado Livre - MongoDB 📦💸
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
  Para executar o projeto é preciso que o Python e o Git estejam instalados, além de mais algumas configurações para o uso do Flask e MongoDB. Para configurar o ambiente virtual, siga o tutorial abaixo:
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
<br>
 
```bash
pip install -r requirements.txt
```

Para acessar os recursos do projeto pode-se utilizar o Insomnia ou o Postman.

</details>

<details>
  <summary>Configurando a conexão com os bancos de dados (MongoDB)</summary>
  Para conectar com o Mongo é preciso alterar o usuário e senha no arquivo connectDatabase em **src/connectDatabase.py**.
<br><br>
 
```python
  db = pymongo.MongoClient("mongodb+srv://<user>:<password>@fa-starting-no-sql.6vnsq.mongodb.net/")
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
A seguir é possível conferir prints do resultado das manipulações no MongoDB para cada documento criado (através do site [https://www.mongodb.com/](https://www.mongodb.com/pt-br)):

| Usuário | ![](https://user-images.githubusercontent.com/69374340/175344828-8a604502-2734-47ed-b27d-a9ec83706380.png) |
|:--------|:-----------------------------------------------------------------------------------------------------------|
| Produto | ![](https://user-images.githubusercontent.com/69374340/175343751-7b39071b-17c4-414a-9ccb-f1f41af3f712.png) ![](https://user-images.githubusercontent.com/69374340/175343860-dab93fc3-9cb6-4f72-b5af-5cae6cdbcb4c.png) |
| Compra  | ![](https://user-images.githubusercontent.com/69374340/175343512-9e8d6f1b-2db6-449c-82d6-6412d6f1b190.png) |
<br>

[![image](https://img.shields.io/badge/✨%20Maria%20Gabriela%20Reis,%202022-LinkedIn-009973?style=flat-square)](https://www.linkedin.com/in/mariagabrielareis/)
