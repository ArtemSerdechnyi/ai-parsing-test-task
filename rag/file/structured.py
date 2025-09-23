from app.file.domain.schemas import ColumnMatches
from rag.file.prompts import build_match_columns_prompt

from rag.model import llm_structured


def match_columns(columns_data: list[dict[str, None]], target_columns: tuple[str, ...]) -> ColumnMatches:
    prompt = build_match_columns_prompt(columns_data, target_columns)

    try:
        matches: ColumnMatches = llm_structured.chat.completions.create(
            model="gpt-5-mini",
            response_model=ColumnMatches,
            messages=[{"role": "user", "content": prompt}],
        )
        return matches
    except Exception as e:
        print(f"Error during AI analysis: {e}")
        # return {"status": "error", "error": str(e)}
        raise
