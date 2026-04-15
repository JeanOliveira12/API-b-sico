from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

class Usuario(BaseModel):
    nome: str
    email: EmailStr
app = FastAPI()

usuarios = []
@app.get("/")
def home():
    return {"message": "Bem-vindo à API de usuários!"}

@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    usuario_dict = usuario.model_dump()

    for u in usuarios:
        if u["email"] == usuario_dict["email"]:
            raise HTTPException(
                status_code=400,
                detail="Email já cadastrado."
            )

    novo_id = max([u["id"] for u in usuarios], default=0) + 1
    usuario_dict["id"] = novo_id

    usuarios.append(usuario_dict)
    return usuario_dict

@app.get("/usuarios")
def listar_usuarios():
    return usuarios

@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    for u in usuarios:
        if u["id"] == usuario_id:
            usuarios.remove(u)
            return {"message": "Usuário deletado com sucesso!"}

    raise HTTPException(status_code=404, detail="Usuário não encontrado.")