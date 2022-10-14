# lab_soft_proj_MEAU

- Nome do Grupo: Grupo 5
- Nome dos Integrantes
    * Augusto Barbosa Villar Silva - 11831853
    * Matheus Tavares de Andrade - 10346662
    * Emilly da Silva Arcanjo - 11808105
# Pré-requisitos

Para utilizar este repositório você precisa ter Python 3.7 instalado e acesso a um terminal de linha de comando.

# Instalação

Primeiramente, abra o seu prompt de comando e clone o repositório através do seguinte comando:

```sh
git clone https://github.com/augustovillar/lab_soft_proj_MEAU.git
```

Após isso, entre na pasta do repositório clonado e ative o ambiente virtual:

```sh
cd lab_soft_proj_MEAU
python -m venv env
```

Para Windows (PowerShell):
```sh
.\env\scripts\Activate.ps1
```

Para Linux e Mac:
```sh
source env/bin/activate
```

É necessário instalar as dependencias no ambiente com o seguinte comando:
```sh
pip install -r requirements.txt
```

Após esse último comando, o nome do seu ambiente deve aparecer no terminal ("env").

# Executando o Programa

Primeiro, o servidor local deve ser configurado. Dentro do diretório "lab_soft_proj_MEAU", execute os seguintes comandos:

```sh
cd Projeto_MEAU
python manage.py runserver
```

Após isso, a aplicação pode ser visualizada no seguinte endereço (acessar via navegador web): [http://localhost:8000/FIRST](http://localhost:8000/FIRST)

Para desativar a aplicação, basta pressionar CTRL + C. Para sair do ambiente virtual (env), basta executar o seguinte comando:

``` sh
deactivate
```

# Executando os Testes
Para a execução dos testes, é necessário iniciar o ambiente do projeto com os sgeuintes comandos:

Para Windows (PowerShell):
```sh
.\env\scripts\Activate.ps1
```

Para Linux e Mac:
```sh
source env/bin/activate
```

Após criar as classes, é preciso criar uma migração e executar a migração. Para isso, na pasta onde está o script manage.py digite:
```sh
python manage.py makemigrations
python manage.py migrate
```

Para executar os teste, é necessário seguir os seguintes passos:

```sh
cd .\Projeto_MEAU\
python manage.py test
```
