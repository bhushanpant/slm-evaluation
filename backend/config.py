"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = "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"

# Council members - list of OpenRouter model identifiers
COUNCIL_MODELS = [
    "openai/gpt-5-nano",
    "google/gemini-2.5-flash-preview-09-2025",
    "anthropic/claude-haiku-4.5",
    "x-ai/grok-4.1-fast:free",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "openai/gpt-5-nano"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
