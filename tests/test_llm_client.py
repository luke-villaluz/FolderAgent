import pytest
from FolderAgent.llm_client import LLMClient


def test_llm_client():
    from FolderAgent.prompt_engine import PromptEngine
    
    prompt_engine = PromptEngine()
    llm_client = LLMClient()
    
    mock_text = "My name is Luke, 1 cool fact is I've seen 46 states, the most common topic I talk about is traveling, and my summary in one sentence is im just a chill dude"
    
    print("Testing LLM Client")
    print("=" * 50)
    print(f"Mock text: {mock_text}")
    print("-" * 30)
    
    # Format the prompt properly using your template
    formatted_prompt = prompt_engine.format_prompt(mock_text)
    print(f"Formatted prompt: {formatted_prompt}")
    
    json_response = llm_client.get_json_response(formatted_prompt)
    
    print("JSON Response:")
    print(json_response)
    print("-" * 30)
    
    assert isinstance(json_response, dict)
    assert "cool_fact" in json_response
    assert "most_common_topic" in json_response
    assert "summary_in_one_sentence" in json_response
    
    print("All required fields present")


if __name__ == "__main__":
    test_llm_client()
