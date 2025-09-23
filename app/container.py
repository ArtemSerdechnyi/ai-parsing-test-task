from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory, Singleton

from app.auth.application.service.jwt import JwtService
from app.file.adapter.output.persistence.repository_adapter import CompanyRepositoryAdapter
from app.file.adapter.output.persistence.sqlalchemy.company import CompanySQLAlchemyRepo
from app.user.adapter.output.persistence.repository_adapter import UserRepositoryAdapter
from app.user.adapter.output.persistence.sqlalchemy.user import UserSQLAlchemyRepo
from app.user.application.service.user import UserService


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(packages=["app"])

    user_repo = Singleton(UserSQLAlchemyRepo)
    user_repo_adapter = Factory(UserRepositoryAdapter, user_repo=user_repo)
    user_service = Factory(UserService, repository=user_repo_adapter)

    company_repo = Singleton(CompanySQLAlchemyRepo)
    company_repo_adapter = Factory(CompanyRepositoryAdapter, company_repo=company_repo)

    jwt_service = Factory(JwtService)
