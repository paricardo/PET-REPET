from src.schemas.customers.customers_schema import *
from src.database.models.customers import Customer



class CustomerService:

    #---------------------------------------
    # SERVIÇO QUE LISTA TODOS OS CLIENTES
    #---------------------------------------
    def get(self):

        customers = Customer.select()

        return [
            CustomerResponseSchema.model_validate(customer)
            for customer in customers
        ]


    #---------------------------------------
    # SERVIÇO QUE LISTA UM CLIENTE
    #---------------------------------------
    def get_by_id(self, id_customer: int):

        customer = Customer.get_or_none(
            Customer.id == id_customer
        )

        if not customer:
            return {"error": "Cliente não encontrado."}, 404

        return CustomerResponseSchema(
            id=customer.id,
            name=customer.name,
            phone=customer.phone,
            email=customer.email,
            notes=customer.notes,
            is_active=customer.is_active,
            created_at=customer.created_at
        ).model_dump()


    #---------------------------------------
    # SERVIÇO QUE CRIA UM CLIENTE NO BANCO
    #---------------------------------------
    def add(self, data, current_customer=None):

        customer_data = CustomerCreateSchema(**data)

        customer = Customer.create(
            name=customer_data.name,
            phone=customer_data.phone,
            email=customer_data.email,
            notes=customer_data.notes
        )

        return CustomerResponseSchema.model_validate(
            customer
        ).model_dump()


    #---------------------------------------
    # SERVIÇO QUE ATUALIZA O CLIENTE NO BANCO
    #---------------------------------------
    def update(self, id_customer: int, data):
        
        customer = Customer.get_or_none(Customer.id == id_customer)

        if not customer:
            return {"error": "Cliente não encontrado"}, 404
        
        customer_data = CustomerUpdateSchema(**data)
        update_data = customer_data.model_dump(exclude_unset=True)

        Customer.update(**update_data).where(Customer.id == id_customer).execute()

        customer = Customer.get(Customer.id == id_customer)

        return CustomerResponseSchema(
            id=customer.id,
            name=customer.name,
            phone=customer.phone,
            email=customer.email,
            notes=customer.notes,
            is_active=customer.is_active,
            created_at=customer.created_at
        ).model_dump()



    #---------------------------------------
    # SERVIÇO QUE DELETA O CLIENTE NO BANCO
    #---------------------------------------
    def delete(self, id_customer: int):
        
        customer = Customer.get_or_none(Customer.id == id_customer)

        if not customer:
            return {"error": "cliente não encontrado"}, 404
        
        customer.delete_instance()

        return {"message": "Cliente removido com sucesso"}






    def activate(self, id_customer: int):
        pass

    def deactivate(self, id_customer: int):
        pass