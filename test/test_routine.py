from pytest_steps import test_steps
import requests

@test_steps(
    'Test Create Routine',
    'Test Retrieve Routine',
    'Test Retrieve Invalid Routine',
    'Test Deactivate Routine'
)
def test_routine():
    payload = {
       "name": "First SEEGE Routine"
    }
    response = requests.post(f'http://localhost:3000/automation/routine', json=payload)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body['name'] == "First SEEGE Routine"
    assert response_body.get('routine_key') is not None
    yield

    routine_key = response_body['routine_key']
    response = requests.get(f'http://localhost:3000/automation/routine/{routine_key}')
    assert response.status_code == 200
    assert response.json()['name'] == 'First SEEGE Routine'
    yield

    invalid_routine_key = '123'
    response = requests.get(f'http://localhost:3000/automation/routine/{invalid_routine_key}')
    assert response.status_code == 404
    assert response.json()['title'] == 'Routine not found'
    yield

    response = requests.delete(f'http://localhost:3000/automation/routine/{routine_key}')
    assert response.status_code == 200
    assert response.json().get('deactivated_on') is not None
    yield
