from datetime import datetime
import uuid
import logging

from models.routine import Routine

class RoutineMapper():
    @staticmethod
    def toDTO(routine_model: Routine) -> dict:
        dto = {
            'name': routine_model.name,
            'routine_key': routine_model.routine_key, 
            'created_at': str(routine_model.created_at)
        }
        if routine_model.deactivated_on is not None:
            dto['deactivated_on'] = str(routine_model.deactivated_on)
        return dto

    def toModel(routine_source: dict) -> Routine:
        model = Routine()
        model.name = routine_source['name']
        model.routine_key = str(uuid.uuid4())
        model.deactivated_on = None
        model.created_at = datetime.now().isoformat()
        return model
