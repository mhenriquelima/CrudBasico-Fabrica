# **CrudBasico-Fabrica: Passo a Passo**

Bem-vindo(a)! Este guia descreve como **executar** o projeto **CrudBasico-Fabrica** localmente, desde a criação do ambiente virtual até a utilização dos endpoints. 

## **1. Pré-Requisitos**

- **Python 3.10+** (ou versão equivalente capaz de rodar o Django 5.1.6)
- **Git** (para clonar o repositório, opcionalmente, ou você pode baixar o ZIP diretamente)
- **pip** (gerenciador de pacotes do Python)

---

## **2. Clonando o Repositório**

Se você tiver o Git instalado, execute:

```bash
git clone https://github.com/jluca-s/CrudBasico-Fabrica.git
```

Caso contrário, acesse o [repositório no GitHub](https://github.com/jluca-s/CrudBasico-Fabrica) e baixe o ZIP do projeto, extraindo-o em uma pasta de sua preferência.

---

## **3. Criando e Ativando o Ambiente Virtual**

Dentro do diretório do projeto `CrudBasico-Fabrica`, crie um ambiente virtual usando o venv (módulo padrão do Python):

### **No Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

### **No Linux/Mac**
```bash
python3 -m venv venv
source venv/bin/activate
```

> **Observação**: Você saberá que o ambiente virtual está ativo quando o prefixo `(venv)` aparecer antes do seu prompt do terminal.

---

## **4. Instalando as Dependências**

Com o ambiente virtual ativo, instale as dependências listadas no arquivo `requiriments.txt`:

```bash
pip install -r requiriments.txt
```

Isto irá instalar as versões necessárias do Django, entre outras dependências requeridas pelo projeto.

---

## **5. Executando as Migrações do Banco de Dados**

O projeto usa um banco de dados **SQLite**. Para gerar as tabelas necessárias, execute:

```bash
python manage.py migrate
```

> Isso criará (ou atualizará) o arquivo `db.sqlite3` na raiz do projeto, aplicando as migrações definidas no app **usuarios** e nas apps internas do Django.

---

## **6. Rodando o Servidor de Desenvolvimento**

Para iniciar o servidor Django (por padrão na porta 8000), execute:

```bash
python manage.py runserver
```

Você verá algo como:

```text
Performing system checks...
System check identified no issues (0 silenced).
February 26, 2025 - ...
Django version 5.1.6, using settings 'projeto.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Abra o navegador e acesse: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## **7. Uso e Descrição dos Endpoints**

Abaixo estão descritas as rotas principais e suas funções. Todas as rotas encontram-se definidas em `projeto/urls.py` e `usuarios/urls.py`.

### **7.1. Visão Geral**

- Todas as rotas abaixo estão **sob o prefixo** `usuarios/`.  
- O app `usuarios` contém as URLs e as *views* que tratam cada funcionalidade do CRUD.

| URL                              | Nome interno        | Método | Descrição                                                                              |
|----------------------------------|---------------------|--------|------------------------------------------------------------------------------------------|
| `/usuarios/`                     | `usuarios:home`     | GET    | Exibe a página **Home** do projeto (informações gerais e links para o CRUD).            |
| `/usuarios/criar/`               | `usuarios:criar`    | GET    | Exibe o formulário para **cadastro** de um novo usuário.                                 |
| `/usuarios/criar/`               | `usuarios:criar`    | POST   | Recebe os dados do formulário e **cria** um novo usuário.                               |
| `/usuarios/listar/`              | `usuarios:listar`   | GET    | **Lista** todos os usuários cadastrados.                                                |
| `/usuarios/detalhe/<int:pk>/`    | `usuarios:detalhe`  | GET    | **Detalhes** de um usuário específico (campo `pk` é o ID do usuário).                   |
| `/usuarios/atualizar/<int:pk>/`  | `usuarios:atualizar`| GET    | Exibe formulário para **atualizar** um usuário específico (por ID).                     |
| `/usuarios/atualizar/<int:pk>/`  | `usuarios:atualizar`| POST   | Recebe os dados atualizados do formulário e **salva** as alterações do usuário.         |
| `/usuarios/deletar/<int:pk>/`    | `usuarios:deletar`  | GET    | **Deleta** o usuário com o `pk` especificado e faz o redirect para `/listar/`.          |

### **7.2. Fluxo Básico de Uso**

1. **Acessar a Home**:  
   Entre em `http://127.0.0.1:8000/usuarios/` para visualizar a tela inicial com duas opções:  
   - *Listar usuários*  
   - *Criar usuário*
   
2. **Criar Usuário**:  
   Vá em `http://127.0.0.1:8000/usuarios/criar/` para ver o formulário de cadastro.  
   - Preencha os campos requisitados (`Nome, Sobrenome, Email, ...`)  
   - Clique em **Cadastrar**  
   - Em caso de sucesso, será feito o redirecionamento para a lista de usuários.
   
3. **Listar Usuários**:  
   Em `http://127.0.0.1:8000/usuarios/listar/`, você pode ver todos os usuários cadastrados.  
   - Se não houver nenhum usuário cadastrado, será exibida a mensagem de que **“Não existem usuários”**.
   - Cada usuário terá opções: **Detalhes**, **Atualizar** e **Deletar**.

4. **Detalhar Usuário**:  
   Em `http://127.0.0.1:8000/usuarios/detalhe/<id>`, você vê todos os campos do objeto (nome, sobrenome, email etc.).

5. **Atualizar Usuário**:  
   Em `http://127.0.0.1:8000/usuarios/atualizar/<id>`, exibe-se um formulário pré-preenchido com dados do usuário. Altere o que for necessário e clique em **Atualizar**.

6. **Excluir Usuário**:  
   Em `http://127.0.0.1:8000/usuarios/deletar/<id>`, o usuário selecionado será excluído e você será redirecionado de volta à lista de usuários.

---

## **8. Observações Importantes**

- O **arquivo de banco de dados** é `db.sqlite3`, e ele é criado automaticamente após rodar as migrações.  
- As variáveis sensíveis (chave secreta etc.) estão em `projeto/settings.py`. Para produção, você deve usar métodos seguros de armazenamento dessas variáveis (por exemplo, variáveis de ambiente).
- O Django Admin está acessível em [`http://127.0.0.1:8000/admin`](http://127.0.0.1:8000/admin). Caso queira usar o Django Admin, crie um superusuário:
  ```bash
  python manage.py createsuperuser
  ```
  E então acesse com as credenciais criadas.

---

**Autor**: [jluca-s](https://github.com/jluca-s)  
**Versão do Django**: 5.1.6  