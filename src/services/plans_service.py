from src.database.models.plans import Plan
from src.schemas.plans.plan_schema import *


class PlanService:
    
    def get(self):
        
        plans = Plan.select()

        return [
            PlanResponseSchema.model_validate(plan).model_dump()
            for plan in plans
        ]


    def getById(self, id_plan: int):

        plan = Plan.get_or_none(
            Plan.id == id_plan
        )

        if not plan:
            return {"error": "Plano não encontrado."}, 404

        return PlanResponseSchema(
            id=plan.id,
            name=plan.name,
            description=plan.description,
            price=plan.price,
            duration_days=plan.duration_days,
            services_info=plan.services_info,
            is_active=plan.is_active,
            created_at=plan.created_at
        ).model_dump()


    def add(self, data):
        
        plan_data = PlanCreateSchema(**data)

        plan = Plan.create(
            name=plan_data.name,
            description=plan_data.description,
            price=plan_data.price,
            duration_days=plan_data.duration_days,
            services_info=plan_data.services_info
        )

        return PlanResponseSchema.model_validate(
            plan
        ).model_dump()


    def update(self, id_plan: int, data):
        
        plan = Plan.get_or_none(Plan.id == id_plan)

        if not plan:
            return {"error": "Plano não encontrado"}, 404
        
        plan_data = PlanUpdateSchema(**data)
        update_data = plan_data.model_dump(exclude_unset=True)

        Plan.update(**update_data).where(Plan.id == id_plan).execute()

        plan = Plan.get(Plan.id == id_plan)

        return PlanResponseSchema(
            id=plan.id,
            name=plan.name,
            description=plan.description,
            price=plan.price,
            duration_days=plan.duration_days,
            services_info=plan.services_info,
            is_active=plan.is_active,
            created_at=plan.created_at
        ).model_dump()


    def delete(self, id_plan: int):
        
        plan = Plan.get_or_none(Plan.id == id_plan)

        if not plan:
            return {"error": "Plano não encontrado"}, 404
        
        plan.delete_instance()

        return {"message": "Plano removido com sucesso"}, 200