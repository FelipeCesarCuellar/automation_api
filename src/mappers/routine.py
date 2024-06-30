class RoutineMapper():
  @staticmethod
  def toDTO(routine_model):
    dto = {'name': routine_model.name,'routine_key': routine_model.routine_key, 
           'trigger_data': routine_model.trigger_data, 'steps_data': routine_model.steps_data,
           'created_at': routine_model.created_at}
    return dto