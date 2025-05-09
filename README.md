# 📘 Projeto Django - To-Do List ✅
Este é um projeto simples de lista de tarefas desenvolvido com **Django**, criado com o objetivo de aprendizado. O projeto foi desenvolvido acompanhando o tutorial do Jefferson Lobato no YouTube.

## 🚀 Funcionalidades

- ✅ Cadastro de usuários
- 🔐 Login e logout
- 🔁 Alteração de senha
- 📋 Criação de tarefas
- ✏️ Edição de tarefas
- ✅ Marcar tarefas como concluídas
- 🗑️ Exclusão de tarefas
- 🗃️ Arquivar tarefas
- 🧑‍💻 Cada usuário vê apenas suas próprias tarefas
- 🎨 Interface web simples e funcional

## 🛠️ Tecnologias utilizadas

- Python 🐍
- Django 🧩
- HTML & CSS 🖌️
- Bootstrap 5 (Sendo carregado pela pasta static) 🖌️
- SQLite (banco de dados padrão do Django)

## ▶️ Como executar o projeto

1. Clone o repositório:
```bash
   git clone https://github.com/emanuel07mii/project_to_do_list.git
```
- Acesse a pasta raiz
```bash
   cd to-do-list
```
2. Crie um ambiente virtual
```bash
   python -m venv venv
```
- Ative o ambiente virtual (Linux/MacOS)
```bash
source venv/bin/activate
```
- Ative o ambiente virtual (Windows)
```bash
venv\Scripts\activate
```
3. Execute as migrações:
```bash
python manage.py migrate
```
4. Inicie o servidor:
```bash
python manage.py runserver
```
5. Acesse:
http://127.0.0.1:8000/

## 👤 Controle de usuários

- Página de registro de novos usuários

- Sistema de login e logout

- Alteração de senha

- Proteção das tarefas por usuário: cada um vê apenas as suas

## 📚 Referência

Curso: Curso de Django (To-Do-List) [📺 Assista no YouTube](https://youtu.be/AdkudhWWMoM?si=XDj3B9FWnEj8Vqij)

### 📌 Observações

- Este projeto foi criado apenas com fins educacionais, como forma de praticar os conceitos do Django.
Créditos ao [Jefferson Lobato](https://www.youtube.com/@JeffersonLobato) pelo excelente conteúdo.

## 📷 Capturas de tela

- Tela Inicial (Sem login)
---
![Home](https://i.postimg.cc/PrrWt70n/inicial-deslogado.png)

- Tela de cadastro de Usuário
---
![Cadastro de Usuário](https://i.postimg.cc/qqQ2schF/registar.png)

- Tela de Log In
---
![Log In](https://i.postimg.cc/SKGGmzkD/login.png)

- Tela Inicial (Logado)
---
![Home Conectado](https://i.imgur.com/OneilSZ.png)

- Tela de tarefas arquivadas
---
![Tarefas Arquivadas](https://i.imgur.com/SAhGUDw.png)

- Tela de Reset de Senha
---
![Redefinir Senha](https://i.postimg.cc/fbXX2QSm/reset-senha.png)
