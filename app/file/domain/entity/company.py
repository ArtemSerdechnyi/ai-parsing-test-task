from pydantic import BaseModel, Field, ConfigDict
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, Session

from core.db import Base


class Company(Base):
    __tablename__ = "company"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    company_name: Mapped[str] = mapped_column(String(255), nullable=False)
    domain_name: Mapped[str] = mapped_column(String(255), nullable=False)

    @classmethod
    def create(cls, *, company_name: str, domain_name: str) -> "Company":
        return cls(company_name=company_name, domain_name=domain_name)


class CompanyRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="Company ID")
    company_name: str = Field(..., title="Company Name")
    domain_name: str = Field(..., title="Domain Name")
