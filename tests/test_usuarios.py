from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_criar_usuario():
    response = client.post("/usuarios", json={
        "nome": "Jean",
        "email": "jean@email.com"
    })
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["nome"] == "Jean"
    assert data["email"] == "jean@email.com"
    assert "id" in data


def test_listar_usuarios():
    response = client.get("/usuarios")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_deletar_usuario():
    # cria usuário primeiro
    response = client.post("/usuarios", json={
        "nome": "Teste",
        "email": "teste@email.com"
    })
    
    user_id = response.json()["id"]

    # deleta
    delete = client.delete(f"/usuarios/{user_id}")
    
    assert delete.status_code == 200
    assert delete.json()["message"] == "Usuário deletado com sucesso!"


def test_usuario_sem_nome():
    response = client.post("/usuarios", json={
        "email": "erro@email.com"
    })
    
    assert response.status_code == 422