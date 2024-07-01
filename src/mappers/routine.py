from datetime import datetime
import uuid

from models.routine import Routine


class RoutineMapper():
  @staticmethod
  def toDTO(routine_model: Routine) -> dict:
    dto = {'name': routine_model.name,'routine_key': routine_model.routine_key, 
           'trigger_data': routine_model.trigger_data, 'steps_data': routine_model.steps_data,
           'created_at': routine_model.created_at}
    return dto
  
  def toModel(routine_source: dict) -> Routine:
    model = Routine()
    model.name = routine_source['name']
    model.routine_key = str(uuid.uuid4())
    model.trigger_data = routine_source['trigger_data']
    model.steps_data = routine_source['steps_data']
    model.created_at = datetime.now().isoformat()

    return model
