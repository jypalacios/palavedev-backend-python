from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repository.login_repository import LoginRepository
from app.utils.permissions import obtener_permisos
from app.auth.jwt import crear_token


class AuthService:

    @staticmethod
    def autenticar(
        db: Session,
        nom_login: str,
        password: str
    ):

        usuario = LoginRepository.obtener_login(
            db,
            nom_login
        )

        if usuario is None:

            raise HTTPException(
                status_code=401,
                detail="Usuario o contraseña incorrectos"
            )

        if usuario.password != password:

            raise HTTPException(
                status_code=401,
                detail="Usuario o contraseña incorrectos"
            )

        permisos = obtener_permisos(
            usuario.nom_rol
        )

        token = crear_token({
            "sub": str(usuario.id_login),
            "nom_login": usuario.nom_login,
            "id_rol": usuario.id_rol,
            "nom_rol": usuario.nom_rol,
            "permisos": permisos
        })

        return {
            "access_token": token,
            "token_type": "bearer",

            "id_login": usuario.id_login,
            "nom_login": usuario.nom_login,

            "id_rol": usuario.id_rol,
            "nom_rol": usuario.nom_rol,

            "permisos": permisos
        }