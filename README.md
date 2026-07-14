# 🏁 Premium Motors

A Premium Motors é uma plataforma web para concessionárias de carros novos, seminovos e usados. Possui catálogo de veículos moderno com filtros de busca (marca, preço, ano), página de detalhes com galeria de fotos e formulário de propostas. Inclui painel administrativo seguro para gestão do estoque e banco PostgreSQL para alta performance.

---

## 🛠️ Tecnologias Utilizadas

*   **Backend:** Python 3.12+ e Django 6.0+
*   **Banco de Dados:** PostgreSQL (Pronto para Produção) / SQLite (Ambiente Local)
*   **Frontend:** HTML5, CSS3 e Bootstrap 5 (Estilização temática de alta performance/corrida)
*   **Segurança:** Python-dotenv para isolamento de credenciais e chaves sensíveis

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com
cd premiumMotors.django
```

### 2. Configurar o Ambiente Virtual (`venv`)
```bash
python -m venv venv
# No Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# No Linux/Mac:
source venv/bin/activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente
Crie um arquivo chamado `.env` na raiz do projeto e configure suas chaves:
```text
SECRET_KEY=sua_chave_secreta_aqui
DEBUG=True
DB_NAME=premiummotors_db
DB_USER=postgres
DB_PASSWORD=sua_senha_do_postgres
DB_HOST=localhost
DB_PORT=5432
```
*(Nota: Graças à configuração híbrida do projeto, se o `DEBUG` estiver como `True`, o Django utilizará automaticamente o banco SQLite local, facilitando o desenvolvimento imediato).*

### 5. Executar as Migrações e Inicializar o Servidor
```bash
python manage.py migrate
python manage.py runserver
```
Acesse o projeto em: [http://127.0.0](http://127.0.0)

---

## 🎛️ Acesso ao Painel Administrativo

Para cadastrar marcas e veículos no estoque do grid de largada, crie um usuário administrador executando:
```bash
python manage.py createsuperuser
```
Acesse o painel em: [http://127.0.0admin/](http://127.0.0admin/)

---
🎨 *Design temático inspirado na estética de automobilismo e carros de corrida.*
