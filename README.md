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

- Tela para alteração de senha

- Proteção das tarefas por usuário: cada um vê apenas as suas

## 📚 Referência

Curso: Curso de Django (To-Do-List) [📺 Assista no YouTube](https://youtu.be/AdkudhWWMoM?si=XDj3B9FWnEj8Vqij)

### 📌 Observações

- Este projeto foi criado apenas com fins educacionais, como forma de praticar os conceitos do Django.
Créditos ao [Jefferson Lobato](https://www.youtube.com/@JeffersonLobato) pelo excelente conteúdo.

## 📷 Capturas de tela

- Tela Inicial (Sem login)
![Home](https://drive.google.com/file/d/1z8g70dxhLVITWP4RoydQcrQJ1NR-Cf68/view?usp=sharing)

- Tela de cadastro de Usuário
![Cadastro de Usuário](https://drive.google.com/file/d/1wd3JMp2AXPJ8uHO4TWfcD58gdDtKtleE/view?usp=drive_link)

- Tela de Log In
![Log In](https://drive.google.com/file/d/1rw6leCvpjS677KPyblBBIlOtD3GedbJF/view?usp=sharing)

- Tela Inicial (Logado)
![Home Conectado](https://drive.google.com/file/d/1tZnVjBmzcJprT9fXilFRFCpdjfNncRQw/view?usp=sharing)

- Tela de tarefas arquivadas
![Tarefas Arquivadas](https://drive.google.com/file/d/1GecOvOVOKS60jsISIOKZAVh6zVveFt8T/view?usp=sharing)

- Tela de Reset de Senha
![Redefinir Senha](https://drive.google.com/file/d/1JvFTCxD-tdKObHSnpsOpd41kpm5cs4Aj/view?usp=sharing)
