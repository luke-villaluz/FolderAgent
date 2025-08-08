import os
from dotenv import load_dotenv

load_dotenv()

INPUT = os.getenv("INPUT")
OUTPUT = os.getenv("OUTPUT")
PROMPT = os.getenv("PROMPT")