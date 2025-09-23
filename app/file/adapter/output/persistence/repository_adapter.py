from app.file.domain.entity.company import CompanyRead, Company
from app.file.domain.repository.company import CompanyRepo


class CompanyRepositoryAdapter:
    def __init__(self, *, company_repo: CompanyRepo):
        self.company_repo = company_repo

    async def get_companies(
        self,
        *,
        limit: int = 12,
        prev: int | None = None,
    ) -> list[CompanyRead]:
        companies = await self.company_repo.get_companies(limit=limit, prev=prev)
        return [CompanyRead.model_validate(c) for c in companies]

    async def get_company_by_id(self, *, company_id: int) -> Company | None:
        return await self.company_repo.get_company_by_id(company_id=company_id)

    async def save(self, *, company: Company) -> None:
        await self.company_repo.save(company=company)

    async def bulk_save(self, *, companies: list[Company]) -> None:
        await self.company_repo.bulk_save(companies=companies)
