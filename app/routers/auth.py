from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.auth import LoginRequest
from app.schemas.auth import LoginResponse
from app.services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)


@router.post(
    "/login",
    response_model=LoginResponse
)
def login(
    datos: LoginRequest,
    db: Session = Depends(get_db)
):

    return AuthService.autenticar(
        db=db,
        nom_login=datos.nom_login,
        password=datos.password
    )