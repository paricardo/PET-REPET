# 🐾 Sistema de Gestão para Pet Shop

Sistema web desenvolvido com Flask para gerenciamento de clientes, pets, serviços, planos e atendimentos.

O objetivo do projeto é fornecer uma solução simples e eficiente para controle operacional do pet shop, permitindo cadastro de clientes e seus pets, gerenciamento de serviços, contratação de planos e agendamento de atendimentos.

---

## 📋 Funcionalidades

### Dashboard
- Visão geral do sistema
- Quantidade de clientes cadastrados
- Quantidade de pets cadastrados
- Quantidade de atendimentos do dia
- Indicadores rápidos

### Clientes
- Cadastro de clientes
- Edição de clientes
- Desativação de clientes
- Histórico de atendimentos
- Consulta de planos contratados

### Pets
- Cadastro de pets
- Edição de pets
- Desativação de pets
- Controle de porte do animal
- Histórico de atendimentos

### Serviços
- Cadastro de serviços
- Preço por porte:
  - Pequeno
  - Médio
  - Grande
- Ativação e desativação de serviços

### Planos
- Cadastro de planos
- Definição de validade
- Valor do plano
- Serviços inclusos
- Controle de planos ativos

### Atendimentos
- Novo agendamento
- Atendimento avulso
- Atendimento por plano
- Cancelamento
- Conclusão de atendimento
- Histórico de atendimentos

### Usuários
- Cadastro de funcionários
- Controle de acesso
- Perfil Administrador
- Perfil Funcionário

---

# 🏗 Arquitetura do Projeto

```text
run.py
config.py

src/
│
├── database/
│   └── in_memory/
│       └── users_in_memory.py
│
├── models/
│   ├── user.py
│   ├── customer.py
│   ├── pet.py
│   ├── service.py
│   ├── plan.py
│   ├── customer_plan.py
│   └── appointment.py
│
├── routes/
│   ├── home_routes.py
│   ├── customer_routes.py
│   ├── pet_routes.py
│   ├── service_routes.py
│   ├── plan_routes.py
│   ├── appointment_routes.py
│   └── user_routes.py
│
├── services/
│   ├── customer_service.py
│   ├── pet_service.py
│   ├── service_service.py
│   ├── plan_service.py
│   ├── appointment_service.py
│   └── user_service.py
│
├── schemas/
│   ├── customer_schema.py
│   ├── pet_schema.py
│   ├── service_schema.py
│   ├── plan_schema.py
│   ├── appointment_schema.py
│   └── user_schema.py
│
├── templates/
│
└── static/
```

---

# 🔄 Fluxo da Aplicação

```text
Formulário HTML
        │
        ▼
Routes
        │
        ▼
Services
        │
        ▼
Schemas
        │
        ▼
Models (Peewee)
        │
        ▼
Banco de Dados
```

---

# 🧩 Camadas da Aplicação

## Routes

Responsáveis por receber as requisições HTTP e encaminhá-las para os serviços.

### Exemplo

```python
@app.route("/clientes")
def listar_clientes():
    return customer_service.listar()
```

---

## Services

Contêm toda a regra de negócio da aplicação.

### Exemplos

- Cadastro de clientes
- Cadastro de pets
- Cadastro de serviços
- Cadastro de planos
- Agendamento de atendimentos
- Cálculo de valores
- Regras de validação

---

## Schemas

Responsáveis pela validação dos dados recebidos pelas rotas.

### Objetivos

- Garantir tipos corretos
- Validar dados obrigatórios
- Evitar informações inválidas
- Padronizar entrada de dados

### Exemplo

```python
class CustomerSchema:
    name: str
    phone: str
    email: str
```

---

## Models

Responsáveis pelo mapeamento das tabelas utilizando Peewee ORM.

### Entidades

- User
- Customer
- Pet
- Service
- Plan
- CustomerPlan
- Appointment

---

# 🗄 Banco de Dados

## Tabelas

### users
Funcionários do sistema.

### customers
Clientes/tutores dos pets.

### pets
Animais vinculados aos clientes.

### services
Serviços oferecidos pelo pet shop.

### plans
Planos disponíveis para contratação.

### customer_plans
Planos contratados pelos clientes.

### appointments
Agendamentos e histórico de atendimentos.

---

# 📅 Fluxo de Atendimento

## Atendimento Avulso

1. Selecionar cliente
2. Selecionar pet
3. Selecionar serviço
4. Identificar porte do pet
5. Calcular valor do serviço
6. Criar agendamento

---

## Atendimento por Plano

1. Selecionar cliente
2. Verificar plano ativo
3. Selecionar pet
4. Selecionar serviço
5. Criar atendimento vinculado ao plano
6. Valor final igual a R$ 0,00

---

# 🖥 Telas do Sistema

- Home
- Clientes
- Pets
- Serviços
- Planos
- Atendimentos
- Novo Atendimento
- Detalhes do Cliente
- Detalhes do Pet
- Detalhes do Plano

---

# 🚀 Tecnologias Utilizadas

- Python 3
- Flask
- Peewee ORM
- PostgreSQL
- Bootstrap 5
- HTML5
- CSS3
- JavaScript

---

# ⚙️ Instalação

## Clonar repositório

```bash
git clone <url-do-repositorio>
```

## Criar ambiente virtual

```bash
python -m venv venv
```

## Ativar ambiente virtual

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar aplicação

```bash
python run.py
```

---

# 🎯 Objetivo do MVP

Entregar uma versão funcional contendo:

- Cadastro de clientes
- Cadastro de pets
- Cadastro de serviços
- Cadastro de planos
- Contratação de planos
- Agendamento de atendimentos
- Histórico de atendimentos
- Dashboard inicial

---

# 🔮 Evoluções Futuras

- Controle de créditos dos planos
- Relatórios financeiros
- Controle de caixa
- Notificações automáticas
- Aplicativo mobile
- Integração com WhatsApp
- Sistema de rotas para busca de pets
- API pública para integração com aplicativos móveis

---

## Autor

Projeto desenvolvido para fins de estudo e aplicação prática em gestão de pet shops utilizando Flask e Peewee ORM.