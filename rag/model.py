from openai import OpenAI
from core.config import config

open_ai_client = OpenAI(
    api_key=config.OPENAI_API_KEY,
)
