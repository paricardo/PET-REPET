from src.database.models.plans import Plans
from src.schemas.plans.plan_schema import *


class PlanService:
    
    def get():
        
        plans = Plans.select()

        return [
            PlanResponseSchema.model_validate(plan)
            for plan in plans
        ]


    def getById(id_plan: int):

        plan = Plans.get_or_none(
            Plans.id == UUID(id_plan)
        )

        if not plan:
            raise ValueError("Serviço não encontrado.")

        return PlanResponseSchema.model_validate(
            plan
        )


    def add(data):
        
        plan_data = PlanCreateSchema(**data)

        plan = Plans.create(
            name=plan_data.name,
            description=plan_data.description,
            price=plan_data.price,
            duration_days=plan_data.duration_days,
            services_info=plan_data.services_info
        )

        return PlanResponseSchema.model_validate(
            plan
        ).model_dump()


    def update(id_plan: int, data):
        
        plan = Plans.get_or_none(Plans.id == id_plan)

        if not plan:
            return {"error": "Plano não encontrado"}, 404
        
        plan_data = PlanUpdateSchema(**data)
        update_data = plan_data.model_dump(exclude_unset=True)

        Plans.update(**update_data).where(Plans.id == id_plan).execute()

        plan = Plans.get(Plans.id == id_plan)

        return PlanResponseSchema(
            id=plan_data.id,
            name=plan_data.name,
            description=plan_data.description,
            price=plan_data.price,
            duration_days=plan_data.duration_days,
            services_info=plan_data.services_info,
            is_active=plan_data.is_active,
            created_at=plan_data.created_at
        ).model_dump()


    def delete(id_plan: int):
        
        plan = Plans.get_or_none(Plans.id == id_plan)

        if not plan:
            return {"error": "Plano não encontrado"}, 404
        
        plan.delete_instance()

        return {"message": "Plano removido com sucesso"}, 200