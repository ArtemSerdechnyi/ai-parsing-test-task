from sqlalchemy import select

from app.file.domain.entity.company import Company
from app.file.domain.repository.company import CompanyRepo
from core.db.session import session_factory


class CompanySQLAlchemyRepo(CompanyRepo):
    async def get_companies(
        self,
        *,
        limit: int = 12,
        prev: int | None = None,
    ) -> list[Company]:
        query = select(Company)
        if prev:
            query = query.where(Company.id < prev)
        if limit > 12:
            limit = 12
        query = query.limit(limit)
        async with session_factory() as read_session:
            result = await read_session.execute(query)
        return result.scalars().all()

    async def get_company_by_id(self, *, company_id: int) -> Company | None:
        async with session_factory() as read_session:
            stmt = await read_session.execute(select(Company).where(Company.id == company_id))
            return stmt.scalars().first()

    async def save(self, *, company: Company) -> None:
        async with session_factory() as write_session:
            write_session.add(company)
            await write_session.commit()

    async def bulk_save(self, *, companies: list[Company]) -> None:
        async with session_factory() as write_session:
            write_session.add_all(companies)
            await write_session.commit()
