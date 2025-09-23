from openai import OpenAI
from instructor import patch
from core.config import config

open_ai_client = OpenAI(
    api_key=config.OPENAI_API_KEY,
)

llm_structured = patch(open_ai_client)
