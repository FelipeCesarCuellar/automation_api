from datetime import datetime
import uuid

from models.routine import Routine

class RoutineMapper():
    @staticmethod
    def toDTO(routine_model: Routine) -> dict:
        dto = {'name': routine_model.name,'routine_key': routine_model.routine_key, 
                'deactivated_on': routine_model.deactivated_on, 'created_at': routine_model.created_at}
        return dto

    def toModel(routine_source: dict) -> Routine:
        model = Routine()
        model.name = routine_source['name']
        model.routine_key = str(uuid.uuid4())
        model.deactivated_on = None #routine_source['deactivated_on']
        model.created_at = datetime.now().isoformat()
        return model
