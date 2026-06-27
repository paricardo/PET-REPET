from uuid import UUID
from src.database.models.customer_plans import CustomerPlan
from src.schemas.customer_plans.customer_plan_schema import *



class CustomerPlanService:

    def get():
        
        customers_plan = CustomerPlan.select()

        return [
            CustomerPlanResponseSchema.model_validate(customer_plan)
            for customer_plan in customers_plan
        ]



    def getById(id_customer_plan: int):
        
        customer_plans = CustomerPlan.get_or_none(
            CustomerPlan.id == UUID(id_customer_plan)
        )

        if not customer_plans:
            raise ValueError("Customer_plan não encontrado.")

        return CustomerPlanResponseSchema.model_validate(
            customer_plans
        )



    def add(data):
        
        customer_plan_data = CustomerPlanCreateSchema(**data)

        customer_plan = CustomerPlan.create(
            customer_id=customer_plan_data.customer_id,
            plan_id=customer_plan_data.plan_id,
            started_at=customer_plan_data.started_at,
            price_paid=customer_plan_data.price_paid
        )

        return CustomerPlanResponseSchema.model_validate(
            customer_plan
        ).model_dump()



    def update(id_customer_plan: int, data):
        
        customer_plans = CustomerPlan.get_or_none(CustomerPlan.id == id_customer_plan)

        if not customer_plans:
            return {"error": "Customer_plan não encontrado"}, 404
        
        customer_plan_data = CustomerPlanUpdateSchema(**data)
        update_data = customer_plan_data.model_dump(exclude_unset=True)

        CustomerPlan.update(**update_data).where(CustomerPlan.id == id_customer_plan).execute()

        customer_plan = CustomerPlan.get(CustomerPlan.id == id_customer_plan)

        return CustomerPlanResponseSchema(
            id=customer_plan_data.id,
            customer_id=customer_plan_data.customer_id,
            plan_id=customer_plan_data.plan_id,
            started_at=customer_plan_data.started_at,
            expires_at=customer_plan_data.expires_at,
            price_paid=customer_plan_data.price_paid,
            status=customer_plan_data.status,
            created_at=customer_plan_data.created_at
        ).model_dump()



    def delete(id_customer_plan: int):
        
        customer_plan = CustomerPlan.get_or_none(CustomerPlan.id == id_customer_plan)

        if not customer_plan:
            return {"error": "Customer_plan não encontrado"}, 404
        
        customer_plan.delete_instance()

        return {"message": "Customer_plan removido com sucesso"}, 200