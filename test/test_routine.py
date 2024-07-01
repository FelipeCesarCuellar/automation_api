from pytest_steps import test_steps
import requests

@test_steps('Test Invalid Key', 'Test Valid Key')

def test_retrieve_routine_by_key():
  routine_key = 'abcde'
  response = requests.get(f'localhost:3000/automation/routine/{routine_key}')
  assert response.status_code == 404
  assert response.json()['title'] == 'Routine not found'
  yield

  routine_key = 'c575cb4f-9828-4470-91d7-665165a75c21'
  response = requests.get(f'localhost:3000/automation/routine/{routine_key}')
  assert response.status_code == 200
  assert response.json()['name'] == 'Teste'
  yield