from sqlalchemy.orm import Session

from app.models.login import LoginView


class LoginRepository:

    @staticmethod
    def obtener_login(
        db: Session,
        nom_login: str
    ):

        return (
            db.query(LoginView)
            .filter(
                LoginView.nom_login == nom_login
            )
            .first()
        )