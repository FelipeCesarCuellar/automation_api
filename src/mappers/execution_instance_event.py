from datetime import datetime
import uuid

from models.execution_instance_event import ExecutionInstanceEvent

class ExecutionInstanceEventMapper():
    @staticmethod
    def toDTO(execution_instance_event_model: ExecutionInstanceEvent) -> dict:
        dto = {'execution_instance_event_key': execution_instance_event_model.execution_instance_event_key,
               'execution_instance_id': execution_instance_event_model.execution_instance_id,
                'created_at': execution_instance_event_model.created_at, 
                'executed_at': execution_instance_event_model.executed_at}
        return dto

    def toModel(execution_instance_event_source: dict) -> ExecutionInstanceEvent:
        model = ExecutionInstanceEvent()
        model.execution_instance_event_key = str(uuid.uuid4())
        model.execution_instance_id = execution_instance_event_source['execution_instance_id']
        model.created_at = datetime.now().isoformat()
        model.executed_at = None
        return model
    