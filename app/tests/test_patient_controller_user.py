def test_get_patients_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" debería poder obtener la lista de productos
    response = test_client.get("/api/patients", headers=user_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_patient(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder crear un nuevo producto
    data = {
        "name": "Guido",
        "last_name": "Zambrana",
        "diagnosis": "artrosis",
        "ci": 14651,
    }
    response = test_client.post("/api/patients", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["name"] == "Guido"
    assert response.json["last_name"] == "Zambrana"
    assert response.json["diagnosis"] == "artrosis"
    assert response.json["ci"] == 14651


def test_create_patient_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder crear un producto
    data = {"name": "Juan", "last_name": "Plata", "diagnosis": "gripe", "ci": 10213}
    response = test_client.post("/api/patients", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_get_patient_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" debería poder obtener un producto específico
    # Este test asume que existe al menos un producto en la base de datos
    response = test_client.get("/api/patients/1", headers=user_auth_headers)
    assert response.status_code == 200
    assert "name" in response.json
    assert "last_name" in response.json
    assert "diagnosis" in response.json
    assert "ci" in response.json


def test_update_patient_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder actualizar un producto
    data = {"name": "Juan", "last_name": "Plata", "diagnosis": "gripe", "ci": 10213}
    response = test_client.put("/api/patients/1", json=data, headers=user_auth_headers)
    assert response.status_code == 403


def test_delete_patient_as_user(test_client, user_auth_headers):
    # El usuario con el rol de "user" no debería poder eliminar un producto
    response = test_client.delete("/api/patients/1", headers=user_auth_headers)
    assert response.status_code == 403