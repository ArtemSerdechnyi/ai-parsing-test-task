from typing import Literal

from pydantic import BaseModel


class ColumnMatch(BaseModel):
    column_index: int
    target_column_name: Literal["company_name", "domain_name"]
    sample_values: list[str]
    is_match: bool
    reason: str


class ColumnMatches(BaseModel):
    matches: list[ColumnMatch]
