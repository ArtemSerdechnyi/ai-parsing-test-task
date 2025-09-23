from app.file.domain.entity.company import Company
from core.db.session import sync_session


def bulk_insert_companies(companies: list[str], domains: list[str]):
    company_objects = [
        Company.create(company_name=c, domain_name=d)
        for c, d in zip(companies, domains)
    ]

    with sync_session() as db:
        db.bulk_save_objects(company_objects)

    print(f"bulk insert {len(company_objects)} companies")

