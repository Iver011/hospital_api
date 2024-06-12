import pytest

# Tests para el controlador de productos


def test_get_patients(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder obtener la lista de productos
    response = test_client.get("/api/patients", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_patient(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder crear un nuevo producto
    data = {
        "name": "Carlos",
        "last_name": "Cordero",
        "diagnosis": "lesion",
        "ci": 145678,
    }
    response = test_client.post("/api/patients", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["name"] == "Carlos"
    assert response.json["last_name"] == "Cordero"
    assert response.json["diagnosis"] == "lesion"
    assert response.json["ci"] == 145678


def test_get_patient(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder obtener un producto específico
    # Este test asume que existe al menos un producto en la base de datos
    response = test_client.get("/api/patients/1", headers=admin_auth_headers)
    assert response.status_code == 200
    assert "name" in response.json


def test_get_nonexistent_patient(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar obtener un producto inexistente
    response = test_client.get("/api/patients/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Paciente no encontrado"


def test_create_patient_invalid_data(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar crear un producto sin datos requeridos
    data = {"name": "Juan"}  # Falta description, price y stock
    response = test_client.post("/api/patients", json=data, headers=admin_auth_headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltan datos requeridos"


def test_update_patient(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder actualizar un producto existente
    data = {
        "name": "Pedro",
        "last_name": "Moreno",
        "diagnosis": "lesion",
        "ci": 14568,
    }
    response = test_client.put("/api/patients/1", json=data, headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["name"] == "Pedro"
    assert response.json["last_name"] == "Moreno"
    assert response.json["diagnosis"] == "lesion"
    assert response.json["ci"] == 14568


def test_update_nonexistent_patient(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar actualizar un producto inexistente
    data = {
        "name": "Juan",
        "last_name": "Aliaga",
        "diagnosis": "resfrio",
        "ci": 14523,
    }
    response = test_client.put(
        "/api/patients/999", json=data, headers=admin_auth_headers
    )
    assert response.status_code == 404
    assert response.json["error"] == "Paciente no encontrado"


def test_delete_patient(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder eliminar un producto existente
    response = test_client.delete("/api/patients/1", headers=admin_auth_headers)
    assert response.status_code == 204

    # Verifica que el producto ha sido eliminado
    response = test_client.get("/api/patients/1", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Paciente no encontrado"


def test_delete_nonexistent_patient(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar eliminar un producto inexistente
    response = test_client.delete("/api/patients/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Paciente no encontrado"