from datetime import datetime
import uuid

from models.execution_event import ExecutionEvent

class ExecutionEventMapper():
    @staticmethod
    def toDTO(execution_model: ExecutionEvent) -> dict:
        dto = {'execution_event_key': execution_model.execution_event_key,'execution_id': execution_model.execution_id, 
                'created_at': execution_model.created_at, 'executed_at': execution_model.executed_at}
        return dto

    def toModel(execution_source: dict) -> ExecutionEvent:
        model = ExecutionEvent()
        model.execution_id= execution_source['execution_id']
        model.execution_event_key = str(uuid.uuid4())
        model.created_at = datetime.now().isoformat()
        model.executed_at = execution_source['executed_at']
        return model
