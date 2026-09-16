from datetime import datetime
from datetime import timedelta
from datetime import timezone

from jose import jwt

from app.config.settings import settings


def crear_token(datos: dict):

    ahora = datetime.now(timezone.utc)

    expiracion = (
        ahora
        + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload = datos.copy()

    payload.update({
        "iat": ahora,
        "exp": expiracion
    })

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )