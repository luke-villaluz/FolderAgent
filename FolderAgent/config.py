import os
from dotenv import load_dotenv

load_dotenv()

INPUT = os.getenv("INPUT")
OUTPUT = os.getenv("OUTPUT")
PROMPT = os.getenv("PROMPT")

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
PERPLEXITY_MODEL = os.getenv("PERPLEXITY_MODEL")
PERPLEXITY_BASE_URL = os.getenv("PERPLEXITY_BASE_URL")