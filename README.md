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

Após isso, entre na pasta do repositório clonado, crie e ative o ambiente virtual:

```sh
cd lab_soft_proj_MEAU
python -m venv env
```

Para ativar o ambiente virtual no Windows (PowerShell):
```sh
.\env\scripts\Activate.ps1
```

Para ativar o ambiente virtual no Linux e Mac:
```sh
source env/bin/activate
```
Com esse último comando, o nome do seu ambiente deve aparecer no terminal ("env").

Por fim, é necessário instalar as dependencias no ambiente com o seguinte comando:
```sh
pip install -r requirements.txt
```

# Executando o Programa

Primeiro, o servidor local deve ser configurado. Dentro do diretório "lab_soft_proj_MEAU", execute os seguintes comandos:

```sh
cd Projeto_MEAU
python manage.py runserver
```

Após isso, a aplicação pode ser visualizada no seguinte endereço (acessar via navegador web): [http://localhost:8000/login](http://localhost:8000/login)

Para acessar as outras telas, use os links da seção "Utilizando o sistema".

Para desativar a aplicação, basta pressionar CTRL + C. 

Para sair do ambiente virtual (env), basta executar o seguinte comando:

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
# Utilizando o sistema

Na tela de login, preencha o campo "usuário" com um dos seguintes nomes para acessar as telas citadas abaixo e clique em "entrar":

- Digite `operador` para acessar a tela de CRUD (criação, remoção, atualização e consulta do cadastro de um voo).
- Digite `funcionario` para acessar a tela de monitoramento, que permite a atualização do status e do horário de chegada e partida real do voo.
- Digite `gerente` para acessar a tela de relatórios.

Para acessar as telas diretamente, use os links listados abaixo.

- [http://localhost:8000/login/](http://localhost:8000/login/)

- [http://localhost:8000/crud/](http://localhost:8000/crud/)
- [http://localhost:8000/atualizar/](http://localhost:8000/atualizar/)
- [http://localhost:8000/modificar/](http://localhost:8000/modificar/)
- [http://localhost:8000/cadastrar/](http://localhost:8000/cadastrar/)
- [http://localhost:8000/consultar/](http://localhost:8000/consultar/)
- [http://localhost:8000/remover/](http://localhost:8000/remover/)
- [http://localhost:8000/visualizavoo/](http://localhost:8000/visualizavoo/)

- [http://localhost:8000/monitoring/](http://localhost:8000/monitoring/)
- [http://localhost:8000/dinamico/](http://localhost:8000/dinamico/)

- [http://localhost:8000/reports/](http://localhost:8000/reports/)
- [http://localhost:8000/preenchimentoAtrasos/](http://localhost:8000/preenchimentoAtrasos/)
- [http://localhost:8000/preenchimentoCancelamentos/](http://localhost:8000/preenchimentoCancelamentos/)
- [http://localhost:8000/relatorio/](http://localhost:8000/relatorio/)

As transições entre as telas do CRUD(criação, remoção, atualização e consulta do cadastro de um voo) podem ser vistas na imagem abaixo. 

![Alt text](Entregas/tela_de_CRUD.png?raw=true "Diagrama tela de CRUD")

As transições entre as telas do monitoramento podem ser vistas na imagem abaixo:

![Alt text](Entregas/tela_de_monitoramento.png?raw=true "Diagrama tela de monitoramento")

As transições entre as telas da geração de relatórios podem ser vistas na imagem abaixo:

![Alt text](Entregas/tela_de_relatorios.png?raw=true "Diagrama tela de relatorios")