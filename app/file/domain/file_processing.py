import re
from itertools import zip_longest
from pathlib import Path

import pandas as pd

from rag.file.structured import match_columns
from app.file.domain.constants import SAMPLES_COUNT, SUBTRACT_COLUMN
from app.file.domain.schemas import ColumnMatches


def preprocess_column_values(values: list[str | None]) -> list[str]:
    processed = []
    for v in values:
        if v:
            v = v.strip().lower()
            v = re.sub(r"[^\w\s.]", "", v)

        processed.append(v)
    return processed


def filter_non_empty_columns(
    company_names: list[str | None],
    domain_names: list[str | None],
) -> tuple[list[str], list[str]]:
    filtered_company = []
    filtered_domain = []

    for company_name, domain_name in zip_longest(company_names, domain_names, fillvalue=None):
        if company_name and domain_name:
            filtered_company.append(company_name)
            filtered_domain.append(domain_name)

    return filtered_company, filtered_domain


def get_column_samples(df: pd.DataFrame, n: int = SAMPLES_COUNT) -> list[dict[str, None]]:
    columns_data = []

    for idx, col in enumerate(df.columns):
        sample_values = df[col].dropna().astype(str).head(n).tolist()
        if not sample_values:
            continue
        columns_data.append({
            "column_index": idx,
            "sample_values": sample_values,
        })

    return columns_data


def extract_columns_by_matches(df: pd.DataFrame, matches: ColumnMatches) -> dict[str, list[str | None]]:
    result = {}

    for m in matches.matches:
        if not m.is_match:
            continue

        data = df.iloc[:, m.column_index].to_list()
        result[m.target_column_name] = data

    return result


def process_files(abm_path: str, sup_path: str):
    abm_path = Path(abm_path)
    sup_path = Path(sup_path)

    target_columns = ["company_name", "domain_name"]

    df_abm = pd.read_excel(abm_path, header=None).replace({pd.NA: None, float("nan"): None})
    df_sup = pd.read_excel(sup_path, header=None).replace({pd.NA: None, float("nan"): None})

    columns_samples_abm = get_column_samples(df_abm)
    columns_samples_sup = get_column_samples(df_sup)

    abm_matches = match_columns(columns_data=columns_samples_abm, target_columns=target_columns)
    sup_matches = match_columns(columns_data=columns_samples_sup, target_columns=target_columns)

    abm_data = extract_columns_by_matches(df_abm, abm_matches)
    sup_data = extract_columns_by_matches(df_sup, sup_matches)

    processed_abm_data = {k: preprocess_column_values(v) for k, v in abm_data.items()}
    processed_sub_data = {k: preprocess_column_values(v) for k, v in sup_data.items()}

    filtered_abm_company, filtered_abm_domain = filter_non_empty_columns(
        processed_abm_data.get("company_name", []),
        processed_abm_data.get("domain_name", []),
    )

    processed_abm_data["company_name"] = filtered_abm_company
    processed_abm_data["domain_name"] = filtered_abm_domain

    sup_domain_set = set(processed_sub_data[SUBTRACT_COLUMN])

    abm_final_companies = []
    abm_final_domains = []

    for c, d in zip(filtered_abm_company, filtered_abm_domain):
        if d not in sup_domain_set:
            abm_final_companies.append(c)
            abm_final_domains.append(d)

    return abm_final_companies, abm_final_domains
