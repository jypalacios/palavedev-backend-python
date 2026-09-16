from sqlalchemy import BigInteger
from sqlalchemy import SmallInteger
from sqlalchemy import String

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class LoginView(Base):

    __tablename__ = "vw_login"

    id_login: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )

    nom_login: Mapped[str] = mapped_column(
        String(50)
    )

    password: Mapped[str] = mapped_column(
        String(255)
    )

    id_rol: Mapped[int] = mapped_column(
        SmallInteger
    )

    nom_rol: Mapped[str] = mapped_column(
        String(20)
    )