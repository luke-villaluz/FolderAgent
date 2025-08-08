import pytest
from FolderAgent.prompt_engine import PromptEngine

def test_prompt_engine():
    prompt_engine = PromptEngine()
    test_combined_text = "this is my combined text"
    
    formatted_prompt = prompt_engine.format_prompt(test_combined_text, "../tests/prompt_engine_test.txt")
    
    # Real assertions
    assert "{COMBINED_TEXT}" not in formatted_prompt
    assert test_combined_text in formatted_prompt
    assert len(formatted_prompt) > len(test_combined_text) 