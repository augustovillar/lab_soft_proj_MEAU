# lab_soft_proj_MEAU

- Nome do Grupo: Grupo 5
- Nome dos Integrantes
    * Augusto Barbosa Villar Silva - 11831853
    * Matheus Tavares de Andrade - 10346662
    * Emilly da Silva Arcanjo - 11808105

# Instalação

Primeiramente, abra o **Powershell** e clone o repositório através do seguinte comando:

```sh
git clone https://github.com/augustovillar/lab_soft_proj_MEAU.git
```

Após isso, entre na pasta do repositório clonado e ative o ambiente virtual:
```sh
cd lab_soft_proj_MEAU
.\env\bin\Activate.ps1
```
Após esse último comando, o nome do seu ambiente deve aparecer no terminal ("env").

# Executando o Programa

Primeiro, o servidor local deve ser configurado. Dentro do diretório "lab_soft_proj_MEAU", execute os seguintes comandos:

```sh
cd Projeto_MEAU
python manage.py runserver
```

Após isso, a aplicação pode ser visualizada no seguinte endereço (acessar via navegador web): [https://localhost:8000/FIRST](https://localhost:8000/FIRST)

Para desativar a aplicação, basta pressionar CTRL + C. Para sair do ambiente virtual (env), basta executar o seguinte comando:

``` sh
deactivate
```