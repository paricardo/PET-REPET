# Modelagem MVP — Pet Shop

> Versão simplificada para entrega rápida. Cobre: usuários, clientes, pets, serviços, agendamentos, planos e histórico.

---

## Visão geral das entidades

```text
users

customers
 └── pets

services

plans

appointments  (liga customer + pet + service + plan?)
```

---

## 1. users

Funcionários que operam o sistema.

| Campo           | Tipo        | Observação                        |
| --------------- | ----------- | --------------------------------- |
| `id`            | UUID / PK   |                                   |
| `name`          | string      |                                   |
| `email`         | string      | único                             |
| `password_hash` | string      |                                   |
| `role`          | enum        | `ADMIN`, `EMPLOYEE`               |
| `is_active`     | boolean     | default `true`                    |
| `created_at`    | datetime    |                                   |

---

## 2. customers

Tutores/donos dos pets.

| Campo        | Tipo      | Observação     |
| ------------ | --------- | -------------- |
| `id`         | UUID / PK |                |
| `name`       | string    |                |
| `phone`      | string    |                |
| `email`      | string    | opcional       |
| `address`    | string    | not null       |
| `notes`      | text      | opcional       |
| `is_active`  | boolean   | default `true` |
| `created_at` | datetime  |                |

| `pets`       | string    |                |
---

## 3. pets

Animais vinculados a um cliente.

| Campo         | Tipo      | Observação                        |
| ------------- | --------- | --------------------------------- |
| `id`          | UUID / PK |                                   |
| `customer_id` | UUID / FK | → customers                       |
| `name`        | string    |                                   |
| `breed`       | string    | opcional                          |
| `size`        | enum      | `SMALL`, `MEDIUM`, `LARGE`        |
| `notes`       | text      | opcional                          |
| `is_active`   | boolean   | default `true`                    |
| `created_at`  | datetime  |                                   |

---

## 4. services

Serviços oferecidos (banho, tosa, hidratação etc.).

| Campo         | Tipo      | Observação                     |
| ------------- | --------- | ------------------------------ |
| `id`          | UUID / PK |                                |
| `name`        | string    | ex: "Banho", "Tosa"            |
| `description` | text      | opcional                       |
| `price_small`  | decimal  | preço para porte SMALL         |
| `price_medium` | decimal  | preço para porte MEDIUM        |
| `price_large`  | decimal  | preço para porte LARGE         |
| `is_active`   | boolean   | default `true`                 |
| `created_at`  | datetime  |                                |

> **Simplificação:** os 3 preços ficam direto na tabela de serviço, sem a tabela `service_prices` separada. Para o MVP isso é suficiente.

---

## 5. plans

Planos/pacotes disponíveis para venda.

| Campo           | Tipo      | Observação                          |
| --------------- | --------- | ----------------------------------- |
| `id`            | UUID / PK |                                     |
| `name`          | string    | ex: "Plano Mensal Básico"           |
| `description`   | text      | opcional                            |
| `price`         | decimal   | valor do plano                      |
| `duration_days` | integer   | ex: `30` para mensal                |
| `services_info` | text/json | descrição livre dos serviços incluídos (ex: "4 banhos + 1 tosa") |
| `is_active`     | boolean   | default `true`                      |
| `created_at`    | datetime  |                                     |

> **Simplificação:** em vez de `package_services`, os serviços incluídos ficam em `services_info` como texto ou JSON simples. Sem controle de crédito por ciclo — isso entra na v2.

---

## 6. customer_plans

Vínculo entre cliente e plano contratado.

| Campo          | Tipo      | Observação                              |
| -------------- | --------- | --------------------------------------- |
| `id`           | UUID / PK |                                         |
| `customer_id`  | UUID / FK | → customers                             |
| `plan_id`      | UUID / FK | → plans                                 |
| `started_at`   | datetime  | início do plano                         |
| `expires_at`   | datetime  | vencimento calculado pelo duration_days |
| `price_paid`   | decimal   | valor pago no momento                   |
| `status`       | enum      | `ACTIVE`, `EXPIRED`, `CANCELED`         |
| `created_at`   | datetime  |                                         |

---

## 7. appointments

Agendamentos e histórico de atendimentos.

| Campo              | Tipo       | Observação                              |
| ------------------ | ---------- | --------------------------------------- |
| `id`               | UUID / PK  |                                         |
| `customer_id`      | UUID / FK  | → customers                             |
| `pet_id`           | UUID / FK  | → pets                                  |
| `service_id`       | UUID / FK  | → services                              |
| `user_id`          | UUID / FK  | → users (quem registrou)                |
| `customer_plan_id` | UUID / FK  | → customer_plans — **nullable**         |
| `scheduled_at`     | datetime   | data/hora do agendamento                |
| `billing_origin`   | enum       | `ONE_TIME`, `PLAN`                      |
| `final_price`      | decimal    | 0 se veio de plano                      |
| `status`           | enum       | `SCHEDULED`, `COMPLETED`, `CANCELED`   |
| `notes`            | text       | opcional                                |
| `created_at`       | datetime   |                                         |

> **Histórico:** filtrar por `status = COMPLETED` e qualquer intervalo de datas em `scheduled_at`. Não precisa de tabela separada.

---

## Enums

```ts
// PetSize
SMALL | MEDIUM | LARGE

// UserRole
ADMIN | EMPLOYEE

// PlanStatus
ACTIVE | EXPIRED | CANCELED

// BillingOrigin
ONE_TIME | PLAN

// AppointmentStatus
SCHEDULED | COMPLETED | CANCELED
```

---

## O que foi simplificado (e por quê)

| Funcionalidade                  | Versão completa                          | MVP                                          |
| ------------------------------- | ---------------------------------------- | -------------------------------------------- |
| Preços por porte                | Tabela `service_prices` separada         | 3 campos direto em `services`                |
| Serviços do plano               | Tabela `package_services`                | Campo `services_info` (texto/JSON)           |
| Ciclos de assinatura            | Tabela `customer_package_cycles`         | Removido — só `expires_at` em `customer_plans` |
| Controle de créditos            | Tabelas `service_credits` + `credit_usages` | Removido — entra na v2                    |
| Histórico separado              | Tabela dedicada                          | Filtro por `status` em `appointments`        |

---

## Fluxos resumidos

### Agendamento avulso
1. Seleciona cliente → pet → serviço
2. Busca preço pelo porte do pet (`price_small / medium / large`)
3. Cria `appointments` com `billing_origin = ONE_TIME`

### Agendamento via plano
1. Seleciona cliente → verifica `customer_plans` com `status = ACTIVE`
2. Seleciona pet → serviço
3. Cria `appointments` com `billing_origin = PLAN`, `final_price = 0`, `customer_plan_id` preenchido

### Histórico do dia
```sql
SELECT * FROM appointments
WHERE scheduled_at::date = CURRENT_DATE
ORDER BY scheduled_at ASC;
```

### Histórico por cliente
```sql
SELECT * FROM appointments
WHERE customer_id = :id
  AND status = 'COMPLETED'
ORDER BY scheduled_at DESC;
```