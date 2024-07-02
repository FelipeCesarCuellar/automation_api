from datetime import datetime
import uuid

from models.execution import Execution

class ExecutionMapper():
    @staticmethod
    def toDTO(execution_model: Execution) -> dict:
        dto = {'name': execution_model.name,'routine_key': execution_model.routine_key, 
                'deactivated_on': execution_model.deactivated_on, 'created_at': execution_model.created_at}
        return dto

    def toModel(execution_source: dict) -> Execution:
        model = Execution()
        model.name = execution_source['name']
        model.execution_key = str(uuid.uuid4())
        model.created_at = datetime.now().isoformat()
        model.execution_data = execution_source['execution_data']
        model.routine_id = execution_source['routine_id']
        model.trigger_at = execution_source['trigger_at']
        return model
