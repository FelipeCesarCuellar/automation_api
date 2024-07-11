from datetime import datetime
import uuid

from models.execution_instance import ExecutionInstance

class ExecutionInstanceMapper():
    @staticmethod
    def toDTO(execution_instance_model: ExecutionInstance) -> dict:
        dto = {'execution_instance_key': execution_instance_model.execution_instance_key, 
                'execution_id': execution_instance_model.execution_id, 
                'created_at': execution_instance_model.created_at,
                'trigger_at': execution_instance_model.trigger_at,
                'triggered_at': execution_instance_model.triggered_at
                }
        return dto

    def toModel(execution_instance_source: dict) -> ExecutionInstance:
        model = ExecutionInstance()
        model.execution_instance_key = str(uuid.uuid4())
        model.execution_id = execution_instance_source['execution_id']
        model.created_at = datetime.now().isoformat()
        model.trigger_at = execution_instance_source['trigger_at']
        model.triggered_at = None
        return model

