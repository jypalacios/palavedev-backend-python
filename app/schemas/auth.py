from pydantic import BaseModel


class LoginRequest(BaseModel):

    nom_login: str
    password: str


class LoginResponse(BaseModel):

    access_token: str
    token_type: str

    id_login: int
    nom_login: str

    id_rol: int
    nom_rol: str

    permisos: list[str]