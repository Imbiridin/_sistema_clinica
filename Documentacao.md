# Django -> https://www.djangoproject.com/

# Comandos principais

1. Criando um ambiente virtual -> python -m venv venv
2. Ativando o ambiente virtual -> venv\Scripts\activate
3. Instalar o django no projeto -> pip install django
4. Para criar um projeto Django -> django-admin startproject project .
5. Para subir o servidor -> python manage.py runserver
6. Para criar um novo app -> python manage.py startapp sistema
7. oara criar um superuser -> python manager.py createsuperuser
8. Para alterar a senha, caso você esqueça -> python manage.py changepassword nomedousuario
9. Para instalar o Pillow no projeto -> python -m pip install Pillow
10. Para gerar o pacotte de imogração -> python manage.py makemigrations
11. Para rodar as alterações desse pacote -> python manage.py migrate
12. Para coletar todos os arquivos estáticos do projeto -> python manage.py collectstatic

# PRINCIPAIS ARQUIVOS/PASTAS DO PROJECT
1. settings.py -> é o arquivo de configuração do projeto.
2. urls.py -> é o arquivo base [principal] de urls do projeto.

# DOCUMENTAÇÃO
1. `urls` -> https://docs.djangoproject.com/en/5.1/topics/http/urls/
2. `settings` -> https://docs.djangoproject.com/en/5.1/topics/settings/ , https://docs.djangoproject.com/en/5.1/ref/settings/



# Criação das entidades do sitema

[PACIENTE]
nome
sobrenome
email
telefone
criação
mensagem
ativo
imagem

[ESPECIALIDADE]
ortopedida
cardiologia
neurologia
clinico geral

[MÉDICO]
nome
sobrenome
crm
email
data do cadastro do médico
telefone
imagem
ativo
mensagem

[CONSULTA]

[ENDEREÇO]


# Criar uma view que vai renderizar um arquivo chamado seunome.html.
# No seunome.html coloque um h1 com o seu nome.
# Em seguida, crie uma url e chame esse arquivo seunome.html.

## AULA DO DIA 08/04/2025
1. INJEÇÃO DE CONTEXTO -> Utilizando o dicionário 'context' para acessar todos os objetos.
- class Paciente (Modelo - Tabela)
- acessar todos os objetos (instâncias) que foram criadas a partir da class Paiente.
- Renderizar todos esses contatos no arquivo listar.html.

## 1. Incluir alguns comandos no settings.py para tratar as imagens;
## 2. Ir no urls.py e incluir uma rota dinâmica para as imagens;
## 3. Ir no listar.html e incluir o campo imagem;
## 4. 