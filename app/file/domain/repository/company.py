from abc import ABC, abstractmethod

from app.file.domain.entity.company import Company


class CompanyRepo(ABC):
    @abstractmethod
    async def get_companies(
        self,
        *,
        limit: int = 12,
        prev: int | None = None,
    ) -> list[Company]:
        """Get company list"""

    @abstractmethod
    async def get_company_by_id(self, *, company_id: int) -> Company | None:
        """Get company by id"""

    @abstractmethod
    async def save(self, *, company: Company) -> None:
        """Save company"""

    @abstractmethod
    async def bulk_save(self, *, companies: list[Company]) -> None:
        """Bulk save companies"""
